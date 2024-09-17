// Select DOM elements for the start button, next button, and quiz container
const startButton = document.getElementById('start-btn');
const nextButton = document.getElementById('next-btn');
const quizContainer = document.getElementById('question-container');

// Variables to keep track of the shuffled questions and the current question index
let questionsShuffled, currentQuestionIndex;

// Select DOM elements for displaying the question and answer buttons
const questionElement = document.getElementById('question');
const answerButtonsElement = document.getElementById('answer-btns');

// Add event listeners to the start and next buttons
startButton.addEventListener('click', startQuiz);
nextButton.addEventListener('click', () => {
    currentQuestionIndex++; // Move to the next question
    setNextQuestion(); // Load the next question
});

// Function to start the quiz
function startQuiz() {
    // Uncomment the next line for debugging purposes
    // console.log('Quiz started');
    startButton.classList.add('hide'); // Hide the start button
    questionsShuffled = questions.sort(() => Math.random() - 0.5); // Shuffle questions
    currentQuestionIndex = 0; // Reset question index
    quizContainer.classList.remove('hide'); // Show the question container
    setNextQuestion(); // Load the first question
}

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

// Array of questions for the quiz
const questions = [
    {
        question: "When was Restaurant Opened?",
        answers: [
            { text: 'correct year', correct: true },
            { text: getRandomInt(1973, 2024), correct: false },
            { text: getRandomInt(1973, 2024), correct: false },
            { text: getRandomInt(1973, 2024), correct: false }
        ]
    },
    {
        question: "What is Restaurant's main cuisine style?",
        answers: [
            { text: 'Italian', correct: false },
            { text: 'Greek', correct: false },
            { text: 'correct Answer', correct: true },
            { text: 'Asian Fusion', correct: false }
        ]
    },
    {
        question: "Which is a dish from our menu?",
        answers: [
            { text: 'Chicken Parmigiana', correct: false },
            { text: 'correct Answer', correct: true },
            { text: 'Fettuccini Gamberi', correct: false },
            { text: 'Combination Seafood Chow Mein', correct: false }
        ]
    },
    {
        question: "How many vegetarian options do we offer on our menu?",
        answers: [
            { text: getRandomInt(1, 10), correct: false },
            { text: getRandomInt(1, 10), correct: false },
            { text: 'correct Answer', correct: true },
            { text: getRandomInt(1, 10), correct: false }
        ]
    },
    {
        question: "Which of the following is one of our dessert specialties?",
        answers: [
            { text: 'Tiramisu', correct: false },
            { text: 'correct Answer', correct: true },
            { text: 'Chocolate Lava Cake', correct: false },
            { text: 'Crème Brûlée', correct: false }
        ]
    },
    {
        question: "Which of the following dietary preferences does Restaurant cater to?",
        answers: [
            { text: 'Gluten-free', correct: false },
            { text: 'Vegan', correct: false },
            { text: 'correct Answer', correct: true },
            { text: 'All of the above', correct: false }
        ]
    },
    {
        question: "Which suburb is Restaurant located in?",
        answers: [
            { text: 'correct Suburb', correct: true },
            { text: 'Suburb 1', correct: false },
            { text: 'Suburb 2', correct: false },
            { text: 'Suburb 3', correct: false }
        ]
    }
];
