class Quiz:
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

    def display(self):
        print()
        print(self.question)
        print()

        for i, choice in enumerate(self.choices, start=1):
            print(f"{i}. {choice}")

    def is_correct(self, user_answer):
        return user_answer == self.answer


default_quizzes = [
    Quiz(
        "Python의 창시자는 누구인가요?",
        ["Guido van Rossum", "Linus Torvalds", "James Gosling", "Bjarne Stroustrup"],
        1
    ),
    Quiz(
        "Python에서 문자열 자료형은 무엇인가요?",
        ["int", "str", "bool", "list"],
        2
    ),
    Quiz(
        "조건에 따라 다른 동작을 하게 할 때 사용하는 문법은 무엇인가요?",
        ["for", "while", "if", "def"],
        3
    ),
    Quiz(
        "반복해서 여러 번 실행할 때 자주 사용하는 문법은 무엇인가요?",
        ["print", "input", "loop", "for"],
        4
    ),
    Quiz(
        "Python에서 리스트를 나타내는 기호는 무엇인가요?",
        ["()", "{}", "[]", "<>"],
        3
    )
]


class QuizGame:
    def __init__(self, quizzes):
        self.quizzes = quizzes
        self.best_score = None

    def show_menu(self):
        print("========================================")
        print("        🎯 나만의 퀴즈 게임 🎯")
        print("========================================")
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 목록")
        print("4. 점수 확인")
        print("5. 종료")
        print("========================================")

    def run(self):
        while True:
            self.show_menu()
            choice = input("선택: ")

            if choice == "1":
                print("퀴즈 풀기 기능은 아직 준비 중입니다.")
            elif choice == "2":
                print("퀴즈 추가 기능은 아직 준비 중입니다.")
            elif choice == "3":
                print("퀴즈 목록 기능은 아직 준비 중입니다.")
            elif choice == "4":
                print("점수 확인 기능은 아직 준비 중입니다.")
            elif choice == "5":
                print("프로그램을 종료합니다.")
                break
            else:
                print("잘못된 입력입니다. 1~5 중에서 선택하세요.")


def main():
    game = QuizGame(default_quizzes)
    game.run()


main()