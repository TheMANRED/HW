from models.models import Plant, Employee, Salon


class Controller:

    @classmethod
    def menu(cls):
        while True:
            print("\n1. Add new plant \n"
                  "2. Get all plants\n"
                  "3. Get plant by id\n"
                  "4. Delete plant by id\n"
                  "5. Add new employee\n"
                  "6. Get all employee\n"
                  "7. Get employee by id\n"
                  "8. Delete employee by id\n"
                  "9. Add new salon\n"
                  "10. Get all salons\n"
                  "11. Get salon by id\n"
                  "12. Delete salon by id\n"
                  )
            flag = int(input("Choose: "))

            if flag == 1:
                cls.new_plant()
            elif flag == 2:
                cls.get_all_plants()
            elif flag == 3:
                cls.get_plants_by_id()
            elif flag == 4:
                cls.delete_plant_by_id()
            elif flag == 5:
                cls.add_new_employee()
            elif flag == 6:
                cls.get_all_employee()
            elif flag == 7:
                cls.get_employee_by_id()
            elif flag == 8:
                cls.delete_employee_by_id()
            elif flag == 9:
                cls.new_salon()
            elif flag == 10:
                cls.get_all_salons()
            elif flag == 11:
                cls.get_salon_by_id()
            elif flag == 12:
                cls.delete_salon_by_id()

            else:
                print("\nWrong choose!\n")

    # ----------------------------------------------------------------------------------------------------------------------

    @classmethod
    def new_plant(cls):
        name = input("Type name of new plant: ")
        location = input("Type location of plant: ")
        plant = Plant(name, location)
        plant.save()

    @classmethod
    def get_all_plants(cls):
        plants = Plant.get_all()
        for plant in plants:
            print(plant["id"])
            print(plant["name"])
            print(plant["location"])

    @classmethod
    def get_plants_by_id(cls):
        id = int(input('Type id of plant: '))
        plant = Plant.get_by_id(id)
        print(plant["id"])
        print(plant["name"])
        print(plant["location"])

    @classmethod
    def delete_plant_by_id(cls):
        id = int(input('Type id of plant which you want to delete: '))
        Plant.delete(id)

    @classmethod
    def add_new_employee(cls):
        name = input("Type name of employee: ")
        email = input("Type email of employee: ")
        plant_id = int(input("Type id of plant: "))
        salon_name = str(input("Type name of salon: "))
        employee = Employee(name, email, plant_id, salon_name)
        salon = Salon.get_by_name(salon_name)
        if not salon:
            raise Exception('Salon doesnt find')
        employee.save()

    @classmethod
    def get_all_employee(cls):
        employees = Employee.get_all()
        for employee in employees:
            print(employee["id"])
            print(employee["name"])
            print(employee["email"])

    @classmethod
    def get_employee_by_id(cls):
        id = int(input('Type id of employee: '))
        employee = Employee.get_by_id(id)
        print(employee["id"])
        print(employee["name"])
        print(employee["email"])

    @classmethod
    def delete_employee_by_id(cls):
        id = int(input('Type id of employee: '))
        Employee.delete(id)

    @classmethod
    def new_salon(cls):
        name = input("Type name of new salon: ")
        location = input("Type location of salon: ")
        salon = Salon(name, location)
        salon.save()

    @classmethod
    def get_all_salons(cls):
        salons = Salon.get_all()
        for salon in salons:
            print(salon["id"])
            print(salon["name"])
            print(salon["location"])

    @classmethod
    def get_salon_by_id(cls):
        id = int(input('Type id of salon: '))
        salon = Salon.get_by_id(id)
        print(salon["id"])
        print(salon["name"])
        print(salon["location"])

    @classmethod
    def delete_salon_by_id(cls):
        id = int(input('Type id of salon which you want to delete: '))
        Salon.delete(id)





