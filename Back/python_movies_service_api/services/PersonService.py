from repositories.PersonRepository import PersonRepository

class PersonService(object):
    def __init__(self):
        self.person_repository = personRepository()

    def add_person(self, name,phone,email):
        return self.person_repository.add_person(name,phone,email)

    def get_all_person(self, page, pagesize,name):
        print("...service....name: " +name)
        return self.person_repository.get_all_person(page, pagesize,name)

    def get_person_by_id(self, id):
        return self.person_repository.get_person_by_id(id)

    def update_person(self, id, name,phone,email):
        return self.person_repository.update_person(id, name,phone,email)

    def delete_person(self, id):
        return self.person_repository.delete_person(id)