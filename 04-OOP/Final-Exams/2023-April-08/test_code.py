from project.robots_managing_app import RobotsManagingApp

# # Test code SoftUni
# main_app = RobotsManagingApp()
# print(main_app.add_service('SecondaryService', 'ServiceRobotsWorld'))
# print(main_app.add_service('MainService', 'ServiceTechnicalsWorld'))
# print(main_app.add_robot('FemaleRobot', 'Scrap', 'HouseholdRobots', 321.26))
# print(main_app.add_robot('FemaleRobot', 'Sparkle', 'FunnyRobots', 211.11))
#
# print(main_app.add_robot_to_service('Scrap', 'ServiceRobotsWorld'))
# print(main_app.add_robot_to_service('Sparkle', 'ServiceRobotsWorld'))
#
# print(main_app.feed_all_robots_from_service('ServiceRobotsWorld'))
# print(main_app.feed_all_robots_from_service('ServiceTechnicalsWorld'))
#
# print(main_app.service_price('ServiceRobotsWorld'))
# print(main_app.service_price('ServiceTechnicalsWorld'))
#
# print(str(main_app))
#
# print(main_app.remove_robot_from_service('Scrap', 'ServiceRobotsWorld'))
# print(main_app.service_price('ServiceRobotsWorld'))
# print(main_app.service_price('ServiceTechnicalsWorld'))
#
# print(str(main_app))

main_app = RobotsManagingApp()
print(main_app.add_service('SecondaryService', 'ServiceRobotsWorld'))
print(main_app.add_service('MainService', 'ServiceTechnicalsWorld'))
print(main_app.add_robot('FemaleRobot', 'Scrap', 'HouseholdRobots', 321.26))
print(main_app.add_robot('FemaleRobot', 'Sparkle', 'FunnyRobots', 211.11))
print(main_app.add_robot_to_service('Scrap', 'ServiceRobotsWorld'))

for i in range(1,15):
    name_robot = 'Scrap' + f'{i}'
    weight = i*100.2
    print(main_app.add_robot('FemaleRobot', name_robot, 'HouseholdRobots', weight))
    print(main_app.add_robot_to_service(name_robot, 'ServiceRobotsWorld'))

print(str(main_app))

print(main_app.feed_all_robots_from_service('ServiceRobotsWorld'))
print(main_app.services[0].robots[0].name)
print(main_app.services[0].robots[0].weight)

print(main_app.add_robot("MaleRobot", "Nero", "SomeRobots", 444))
print(main_app.add_robot_to_service('Nero', 'ServiceTechnicalsWorld'))
print(main_app.feed_all_robots_from_service('ServiceTechnicalsWorld'))
print(main_app.services[1].robots[0].name)
print(main_app.services[1].robots[0].weight)

print(main_app.add_robot("MaleRobot", "", "SomeRobots",521))
