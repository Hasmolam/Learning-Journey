
# Soru sınıfı: Bir sorunun metni, şıkları ve doğru cevabını tutar
class Question:
    def __init__(self, text, choices, answer):
        self.text = text  # Soru metni
        self.choices = choices  # Şıklar
        self.answer = answer  # Doğru cevap
    
    def checkAnswer(self, answer):
        # Girilen cevabın doğru olup olmadığını kontrol eder
        return self.answer == answer


# Quiz sınıfı: Soruları yönetir, puan tutar ve kullanıcıya soruları gösterir
class Quiz:
    def __init__(self, questions):
        self.questions = questions  # Soru listesi
        self.score = 0  # Kullanıcının puanı
        self.questionIndex = 0  # Şu anki soru indeksi

    def getQuestion(self):
        # Şu anki soruyu döndürür
        return self.questions[self.questionIndex]

    def displayQuestion(self):
        # Soruyu ve şıkları ekrana yazdırır
        question = self.getQuestion()
        print(f'Soru {self.questionIndex + 1}: {question.text}')

        for q in question.choices:
            print('-' + q)
        
        answer = input('cevap: ')
        self.guess(answer)
        self.loadQuestion()

    def guess(self, answer):
        # Kullanıcının cevabını kontrol eder ve puanı günceller
        question = self.getQuestion()

        if question.checkAnswer(answer):
            self.score += 1
        self.questionIndex += 1

    def loadQuestion(self):
        # Sıradaki soruyu yükler veya quiz bitti ise sonucu gösterir
        if len(self.questions) == self.questionIndex:
            self.showScore()
        else:
            self.displayProgress()
            self.displayQuestion()

    def showScore(self):
        # Kullanıcının toplam puanını ekrana yazdırır
        print('score: ', self.score)

    def displayProgress(self):
        # Quiz ilerlemesini ekrana yazdırır
        totalQuestion = len(self.questions)
        questionNumber = self.questionIndex + 1

        if questionNumber > totalQuestion:
            print('Quiz bitti.')
        else:
            print(f'Question {questionNumber} of {totalQuestion}'.center(100, '*'))

# Soru nesneleri oluşturuluyor
q1 = Question('en iyi programlama dili hangisidir ?', ['C#', 'python', 'javascript', 'java'], 'python')
q2 = Question('en popüler programlama dili hangisidir ?', ['python', 'javascript', 'C#', 'java'], 'python')
q3 = Question('en çok kazandıran programlama dili hangisidir ?', ['C#', 'javascript', 'java', 'python'], 'python')
q4 = Question('en çok sevilen programlama dili hangisidir ?', ['C#', 'javascript', 'java', 'python'], 'python')
q5 = Question('en kolay programlama dili hangisidir ?', ['C#', 'javascript', 'java', 'python'], 'python')

# Sorular bir listeye ekleniyor
questions = [q1, q2, q3, q4, q5]

# Quiz başlatılıyor
quiz = Quiz(questions)

quiz.loadQuestion()  # Quiz başlatılır