
let questions;

(async function() {
    await fetchData();

    console.log("You can now use these questions:", questions);
    console.log(typeof questions)
})();

// Select DOM elements for the start button, next button, and quiz container
const startButton = document.getElementById('start-btn');
const nextButton = document.getElementById('next-btn');
const quizContainer = document.getElementById('question-container');

// Variables to keep track of the shuffled questions and the current question index
let questionsShuffled, currentQuestionIndex;

// Select DOM elements for displaying the question and answer buttons
const questionElement = document.getElementById('question');
const answerButtonsElement = document.getElementById('answer-btns');

async function fetchData() {
    try {
        const response = await fetch("http://127.0.0.1:5000/get-questions");
        if (!response.ok) {
            throw new Error("Network response was not ok");
        }
        questions = await response.json();
        questions = questions.questions
        console.log("Questions set:", questions);
    } catch(error) {
        console.error('There was a problem with the fetch operation:', error);
    }
}

// Add event listeners to the start and next buttons
startButton.addEventListener('click', startQuiz);

nextButton.addEventListener('click', () => {
    currentQuestionIndex++; // Move to the next question
    setNextQuestion(); // Load the next question
});


// Function to start the quiz
function startQuiz(){
    //console.log('Quiz started')
    startButton.classList.add('hide')
    questionsShuffled = questions.sort(() => Math.random() - 0.5)
    questionsShuffled.forEach(question => {
        question.answers = question.answers.sort(() => Math.random() - 0.5)
    })
    currentQuestionIndex = 0
    quizContainer.classList.remove('hide')
    setNextQuestion()

// Function to load the next question
function setNextQuestion() {
    resetState(); // Reset previous state
    showQuestion(questionsShuffled[currentQuestionIndex]); // Display the current question
}

// Function to reset the state of the quiz UI
function resetState() {
    clearStatusClass(document.body); // Clear status classes from the body
    nextButton.classList.add('hide'); // Hide the next button
    // Remove all existing answer buttons
    while (answerButtonsElement.firstChild) {
        answerButtonsElement.removeChild(answerButtonsElement.firstChild);
    }
}

// Function to display a question and its possible answers
function showQuestion(question) {
    questionElement.innerText = question.question; // Set the question text
    question.answers.forEach(answer => {
        const button = document.createElement('button'); // Create a new button for each answer
        button.innerText = answer.text; // Set button text
        button.classList.add('btn'); // Add styling class
        if (answer.correct) {
            button.dataset.correct = answer.correct; // Mark the correct answer
        }
        button.addEventListener('click', selectAnswer); // Add click event listener
        answerButtonsElement.appendChild(button); // Add button to the answer container
    });
}

// Function to handle answer selection
function selectAnswer(e) {
    const selectedButton = e.target; // Get the button that was clicked
    const correct = selectedButton.dataset.correct; // Check if the answer is correct
    setStatusClass(document.body, correct); // Update the body class based on correctness
    Array.from(answerButtonsElement.children).forEach(button => {
        setStatusClass(button, button.dataset.correct); // Update button classes based on correctness
    });
    // Show the next button if there are more questions
    if (questionsShuffled.length > currentQuestionIndex + 1) {
        nextButton.classList.remove('hide');
    } else {
        startButton.innerText = 'Restart'; // Change the start button text to Restart
        startButton.classList.remove('hide'); // Show the start button
    }
}

// Function to set status classes (correct/incorrect) on elements
function setStatusClass(element, correct) {
    clearStatusClass(element); // Remove previous status classes
    if (correct) {
        element.classList.add('correct'); // Add 'correct' class if the answer is correct
    } else {
        element.classList.add('wrong'); // Add 'wrong' class if the answer is incorrect
    }
}

// Function to clear status classes from an element
function clearStatusClass(element) {
    element.classList.remove('correct');
    element.classList.remove('wrong');
}

// Function to generate a random integer between min (inclusive) and max (exclusive)
function getRandomInt(min, max) {
    const minCeiled = Math.ceil(min);
    const maxFloored = Math.floor(max);
    return Math.floor(Math.random() * (maxFloored - minCeiled) + minCeiled); // Return a random integer
}
