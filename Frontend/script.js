let questions;

// Select DOM elements for restaurant form, start button, and next button
const restaurantForm = document.getElementById('restaurant-form');
const restaurantInput = document.getElementById('restaurant-name');
const submitButton = document.getElementById('submit-btn');
const startButton = document.getElementById('start-btn');
const nextButton = document.getElementById('next-btn');
const quizContainer = document.getElementById('question-container');

// Variables to keep track of the shuffled questions and the current question index
let questionsShuffled, currentQuestionIndex;

// Select DOM elements for displaying the question and answer buttons
const questionElement = document.getElementById('question');
const answerButtonsElement = document.getElementById('answer-btns');

// Event listener for the submit button to handle restaurant name submission
submitButton.addEventListener('click', async () => {
    const restaurantName = restaurantInput.value.trim(); // Get the restaurant name entered by the user
    
    if (restaurantName) {
        // Fetch questions for the given restaurant name
        await fetchData(restaurantName);
        
        // Hide the restaurant form and show the start button
        restaurantForm.classList.add('hide');
        startButton.classList.remove('hide');
        
        console.log("You can now use these questions:", questions);
    } else {
        alert('Please enter a restaurant name.');
    }
});

// Event listener for the start button to start the quiz
startButton.addEventListener('click', startQuiz);

// Event listener for the next button to load the next question
nextButton.addEventListener('click', () => {
    currentQuestionIndex++;
    setNextQuestion();
});

// Function to fetch questions based on the restaurant name
async function fetchData(restaurantName) {
    try {
        const response = await fetch(`http://127.0.0.1:5000/get-questions/${restaurantName}`);
        if (!response.ok) {
            throw new Error("Network response was not ok");
        }
        questions = await response.json();
        questions = questions.questions;
        console.log("Questions set:", questions);
    } catch (error) {
        console.error('There was a problem with the fetch operation:', error);
    }
}

// Function to start the quiz
function startQuiz() {
    startButton.classList.add('hide'); // Hide the start button
    questionsShuffled = questions.sort(() => Math.random() - 0.5); // Shuffle the questions
    questionsShuffled.forEach(question => {
        question.answers = question.answers.sort(() => Math.random() - 0.5); // Shuffle the answers
    });
    currentQuestionIndex = 0;
    quizContainer.classList.remove('hide'); // Show the quiz container
    setNextQuestion(); // Load the first question
}

// Function to load the next question
function setNextQuestion() {
    resetState(); // Reset the previous state
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