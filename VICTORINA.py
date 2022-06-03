from pymongo import MongoClient



class DataBase:
	def __init__(self):
		cluster = MongoClient("mongodb+srv://user:12345@cluster0.jgito.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

		self.db = cluster["QuizBot"]
		self.users = self.db["Users"]
		self.questions = self.db["Questions"]

		self.questions_count = len(list(self.questions.find({})))

	def get_user(self, chat_id):
		user = self.users.find_one({"chat_id": chat_id})

		if user is not None:
			return user

		user = {
			"chat_id": chat_id,
			"is_passing": False,
			"is_passed": False,
			"question_index": None,
			"answers": []
		}

		self.users.insert_one(user)

		return user

	def set_user(self, chat_id, update):
		self.users.update_one({"chat_id": chat_id}, {"$set": update})

	def get_question(self, index):
		return self.questions.find_one({"id": index})

db = DataBase()