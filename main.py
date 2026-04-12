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

    def play_quiz(self):
        if not self.quizzes:
            print("등록된 퀴즈가 없습니다.")
            return

        print()
        print(f"📝 퀴즈를 시작합니다! (총 {len(self.quizzes)}문제)")

        score = 0

        for index, quiz in enumerate(self.quizzes, start=1):
            print("----------------------------------------")
            print(f"[문제 {index}]")
            quiz.display()

            user_input = input("정답 입력 (1-4): ").strip()

            if user_input in ["1", "2", "3", "4"]:
                user_answer = int(user_input)

                if quiz.is_correct(user_answer):
                    print("✅ 정답입니다!")
                    score += 1
                else:
                    print(f"❌ 오답입니다! 정답은 {quiz.answer}번입니다.")
            else:
                print("⚠️ 잘못된 입력입니다. 이 문제는 오답 처리됩니다.")

        print("----------------------------------------")
        print(f"🏆 결과: {len(self.quizzes)}문제 중 {score}문제 정답!")

        if self.best_score is None or score > self.best_score:
            self.best_score = score
            print("🎉 새로운 최고 점수입니다!")

    def add_quiz(self):
        print()
        print("📌 새로운 퀴즈를 추가합니다.")

        question = input("문제를 입력하세요: ").strip()
        choice1 = input("선택지 1: ").strip()
        choice2 = input("선택지 2: ").strip()
        choice3 = input("선택지 3: ").strip()
        choice4 = input("선택지 4: ").strip()
        answer_input = input("정답 번호 (1-4): ").strip()

        if answer_input not in ["1", "2", "3", "4"]:
            print("⚠️ 정답 번호는 1~4 사이의 숫자여야 합니다.")
            return

        new_quiz = Quiz(
            question,
            [choice1, choice2, choice3, choice4],
            int(answer_input)
        )

        self.quizzes.append(new_quiz)
        print("✅ 퀴즈가 추가되었습니다!")

    def show_quizzes(self):
        print()

        if not self.quizzes:
            print("등록된 퀴즈가 없습니다.")
            return

        print(f"📋 등록된 퀴즈 목록 (총 {len(self.quizzes)}개)")
        print("----------------------------------------")

        for index, quiz in enumerate(self.quizzes, start=1):
            print(f"[{index}] {quiz.question}")

        print("----------------------------------------")

    def run(self):
        while True:
            self.show_menu()
            choice = input("선택: ").strip()

            if choice == "1":
                self.play_quiz()
            elif choice == "2":
                self.add_quiz()
            elif choice == "3":
                self.show_quizzes()
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