const startButton = document.getElementById('start-btn')
const nextButton = document.getElementById('next-btn')
const quizContainer = document.getElementById('question-container')

let questionsShuffled, currentQuestionIndex

const questionElement = document.getElementById('question')
const answerButtonsElement = document.getElementById('answer-btns')


startButton.addEventListener('click', startQuiz)
nextButton.addEventListener('click', () => {
    currentQuestionIndex++
    setNextQuestion()
})

function startQuiz(){
    //console.log('Quiz started')
    startButton.classList.add('hide')
    questionsShuffled = questions.sort(() => Math.random() - 0.5)
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

const questions = [
    {//name of restaurant and corrent year need to be generated from datatbase
        question: "When was Restaurant Opened?",
        answers: [
            { text: 'correct year', correct: true },
            { text: getRandomInt(1973, 2024)
                , correct: false },
            { text: getRandomInt(1973, 2024)
                , correct: false },
            { text: getRandomInt(1973, 2024)
                , correct: false }
        ]
    }, 
    {
        question: "What is Restaurant's main cuisine style?",
        answers: [
            {text: 'Italian', correct: false}, 
            {text: 'Greek', correct: false}, 
            {text: 'correct Answer', correct: true}, 
            {text: 'Asain Fusion', correct: false}
        ]
    },
    {
        question: "Which is a dish from our menu?",
        answers: [
            {text: 'Chicken Parmigana', correct: false}, 
            {text: 'correct Answer', correct: true}, 
            {text: 'Fettuccini Gamberi', correct: false}, 
            {text: 'Combinbation Sea-food chow mein', correct: false} 
        ]
    },
    {
        question: "How many vegetarian options do we offer on our menu?",
        answers: [
            {text: getRandomInt(1, 10), correct: false}, 
            {text: getRandomInt(1, 10), correct: false}, 
            {text: 'correct Answer', correct: true}, 
            {text: getRandomInt(1, 10), correct: false}
        ]
    },
    {
        question: "Which of the following is one of our dessert specialties?",
        answers: [
            {text: 'Tiramisu', correct: false}, 
            {text: 'correct Answer', correct: true}, 
            {text: 'Chocolate Lava Cake', correct: false}, 
            {text: 'Crème Brûlée', correct: false}
        ]
    },
    {
        question: "Which of the following dietary preferences does Restaurant cater to?",
        answers: [
            {text: 'Gluten-free', correct: false},
            {text: 'Vegan', correct: false}, 
            {text: 'correct Answer', correct: true},  
            {text: 'All of the above', correct: false}
        ]
    },
    {question: "When suburb is Restaurant located?",
        answers: [ //generate random suburbs from city restaurant is located
            {text: 'correct Suburb', correct: true}, 
            {text: 'Suburb 1', correct: false},
            {text: 'Suburb 2', correct: false},  
            {text: 'Suburb 3', correct: false}
        ]
    }
]