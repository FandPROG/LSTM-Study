import os

def showMenu():
    print("=== 나만의 To-Do 리스트 ===\n1. 할 일 추가\n2. 할 일 목록 보기\n3. 할 일 삭제\n4. 저장\n5. 불러오기\n0. 종료")

def addTask():
    global todoList
    s = input("추가할 할 일:").strip()
    if(not s) :
        print("비어있는 입력은 받을 수 없습니다.")
        return
    todoList.append(s)

def viewTasks():
    global todoList
    for i in todoList :
        print(i)

def deleteTask():
    global todoList
    try:
        n = int(input("지울 테스크의 번호를 입력해주세요.."))
        if(n >= len(todoList)) :
            print("숫자가 너무 큽니다!")
        else :
            todoList.pop(n)
    except ValueError :
        print("숫자를 입력해 주세요")
    except Exception as e :
        print(f"오류가 발생했습니다. : {e}")

def saveTasks():
    global todoList
    try:
        with open("todo.txt", "w", encoding="utf-8") as file:
            file.write("\n".join(todoList))
        print("파일이 저장되었습니다.!")

    except FileNotFoundError :
            print("파일을 찾을 수 없습니다. 파일을 확인해 주세요.")
            return
    except Exception as e :
            print(f"오류가 발생했습니다: {e}")
            return

def loadTasks():
    global todoList
    try:
        with open("todo.txt", "r", encoding="utf-8") as file:
            todoList = file.read().split("\n")
            print("파일을 불러왔습니다.")

    except FileNotFoundError :
        print("파일을 찾을 수 없습니다. 파일을 확인해 주세요.")
        return
    except Exception as e :
        print(f"오류가 발생했습니다: {e}")
        return

def main():
    print(os.getcwd())
    global todoList
    todoList = []

    while(True) :
        showMenu()
        try:
            n = int(input(">> "))
            if(n == 1):
                addTask()
            elif(n == 2):
                viewTasks()
            elif(n == 3):
                deleteTask()
            elif(n == 4):
                saveTasks()
            elif(n == 5):
                loadTasks()
            elif(n == 0) :
                break
            else:
                print("1~5 사이의 숫자를 입력해주세요.")
        except ValueError:
            print("올바른 숫자가 아닙니다.")
        except Exception as e:
            print(f"오류가 발생했습니다: {e}")


if __name__ == "__main__":
    main()
