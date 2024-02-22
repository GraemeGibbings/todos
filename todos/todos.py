def addATodo():
    pass

def editAtodo():
    pass

def completeATodo():
    pass

def showTodos():
    pass

def readTodos():
    pass

def writeTodos():
    pass

while True:
    command = input("enter one of the follow: add, edit, complete, show, or exit: ")

    match command:
        case "add":
            addATodo()
        case "edit":
            editAtodo()
        case "complete":
            completeATodo()
        case "show":
            showTodos()
        case "exit":
            break
    
    pass