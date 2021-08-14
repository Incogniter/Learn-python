# to multiply the given number by 2.54 for finding their inches using comperiention

inch_measuremnet = (3, 8, 20)

cm_measurement = [inch * 2.54 for inch in inch_measuremnet]
print(cm_measurement)

# changing the list to a tuple

cm_measurement = tuple([inch * 2.54 for inch in inch_measuremnet])
print(cm_measurement)

