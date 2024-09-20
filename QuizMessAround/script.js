let questions;

(async function() {
    await fetchData();

    console.log("You can now use these questions:", questions);
    console.log(typeof questions)
})();

const startButton = document.getElementById('start-btn')
const nextButton = document.getElementById('next-btn')
const quizContainer = document.getElementById('question-container')

let questionsShuffled, currentQuestionIndex

const questionElement = document.getElementById('question')
const answerButtonsElement = document.getElementById('answer-btns')

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

startButton.addEventListener('click', startQuiz)
nextButton.addEventListener('click', () => {
    currentQuestionIndex++
    setNextQuestion()
})

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
}

function setNextQuestion(){
    resetState()
    showQuestion(questionsShuffled[currentQuestionIndex])
}

function resetState(){
    clearStatusClass(document.body)
    nextButton.classList.add('hide')
    while (answerButtonsElement.firstChild) {
        answerButtonsElement.removeChild(answerButtonsElement.firstChild)
    }
}

function showQuestion(question) {
    questionElement.innerText = question.question
    question.answers.forEach(answer => {
        const button = document.createElement('button')
        button.innerText = answer.text
        button.classList.add('btn')
        if (answer.correct) {
            button.dataset.correct = answer.correct
        }
        button.addEventListener('click', selectAnswer)
        answerButtonsElement.appendChild(button)
    })
}

function selectAnswer(e) {
    const selectedButton = e.target
    const correct = selectedButton.dataset.correct
    setStatusClass(document.body, correct)
    Array.from(answerButtonsElement.children).forEach(button => {
        setStatusClass(button, button.dataset.correct)
    })
    if (questionsShuffled.length > currentQuestionIndex + 1) {
        nextButton.classList.remove('hide')
    } else {
        startButton.innerText = 'Restart'
        startButton.classList.remove('hide')
    }
}

function setStatusClass(element, correct){
    clearStatusClass(element)
    if (correct) {
        element.classList.add('correct')
    } else {
        element.classList.add('wrong')
    }
}

function clearStatusClass(element) {
    element.classList.remove('correct')
    element.classList.remove('wrong')
}

function getRandomInt(min, max) {
    const minCeiled = Math.ceil(min);
    const maxFloored = Math.floor(max);
    return Math.floor(Math.random() * (maxFloored - minCeiled) + minCeiled); // The maximum is exclusive and the minimum is inclusive
  }