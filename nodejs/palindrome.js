// Palindrome Checker in nodejs

const readline = require('readline')

const question = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})

function isPalindrome(word) {
    const cleanedWord = word.replace(/[^a-zA-Z0-9]/g, "").toLowerCase()
    const reversedWord = cleanedWord.split('').reverse().join('')
    return cleanedWord == reversedWord
}

question.question("Type a word: ", (word) => {

    if (word.trim == "0") {
        question.close()
    }

    console.log(isPalindrome(word) ? "It's a palindrome" : "Not is a palindrome")
    question.close()
})