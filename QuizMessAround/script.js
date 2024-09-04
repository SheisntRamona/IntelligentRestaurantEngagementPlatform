const startButton = document.getElementById('start-btn')
const quizContainer = document.getElementById('question-container')

let questionsShuffled, currentQuestionIndex

const questionElement = document.getElementById('question')
const answerButtons = document.getElementById('answer-buttons')


startButton.addEventListener('click', startQuiz)

function startQuiz(){
    //console.log('Quiz started')
    startButton.classList.add('hide')
    questionsShuffled = questions.sort(() => Math.random() - 0.5)
    currentQuestionIndex = 0
    quizContainer.classList.remove('hide')
    nextQuestion()
}

function nextQuestion(){
    showQuestion(questionsShuffled[currentQuestionIndex])
}

function showQuestion(question) {
    questionElement.innerText = question.question
}

function selectAnswer() {

}

//implement text gen later
const questions = [
    {
        //name of restaurant needs to be generated from datatbase
        question: "When was Restaurant Opened?",
        answers: [
            { text: 'year', correct: true },
            { text: 'year2', correct: false },
            { text: 'year3', correct: false },
            { text: 'year4', correct: false }
        ]
    }
]