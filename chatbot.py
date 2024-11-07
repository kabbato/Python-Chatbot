from nltk.chat.util import Chat, reflections

pairs = [
    ['My name is (.*)', ['Hi %1']],
    ['What is your name?', ['My nam is HAL']],
    ['(hi|hello|hey|howdy)', ['hey there', 'hello', 'greetings']],
    ['(.*) in (.*) is fun', ['%1 in %2 is super fun']],
    ['(.*)(location|city) ?', ['Rome, Italy']],
    ['Who created you?', ['kabbato did']],
    ['How is the weather in (.*)', ['The weather in %1 is great', 'The weather in %1 is not the best']]

]

reflections.update({'go': 'gone', 'You need' : 'I need'})

chat = Chat(pairs, reflections)
chat.converse()
