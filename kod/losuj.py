# -*- encoding: utf-8 -*-
# kod w pythonie do losowania studentów

import yaml
import random
import pandas as pd

def losuj(week, listob='listob.xlsx', role='role.yaml'):
	# wczytujemy role
	with open(role, encoding='utf-8') as f:
		role = yaml.load(f)
	all_klasa = list()
	weeks = list(role.keys())
	weeks.sort()

	# wczytujemy listę obecności
	df = pd.read_excel(listob)
	all_osoby = list(df.loc[:, 'Imię i nazwisko'])
	wylosowani = dict()

	all_roles = ['klasa', 'platforma', 'prezentacja']
	for rola in all_roles:
		osoby = list(all_osoby)
		wykonane = list()
		for w in weeks:
			wykonane += role[w][rola]
			if int(w[-1]) == week:
				obecne_role = role[w][rola]

		# usuwamy 'None'
		remove_all(wykonane, 'None')
		remove_all(obecne_role, 'None')

		# usuwamy osoby, które już były:
		for name in wykonane:
			osoby.remove(name)

		# losujemy
		wylosuj = 2 - len(obecne_role)
		wylosowani[rola] = random.sample(osoby, wylosuj) + obecne_role
	print_wylosowani(week, wylosowani)
	return wylosowani

def print_wylosowani(week, wylosowani):
	print('week_0{}:'.format(week))
	for rola in wylosowani.keys():
		print('   {}: {}'.format(rola, wylosowani[rola]))

def remove_all(lst, value):
	'''remove all values from list in-place'''
	num_rem = lst.count(value)
	for i in range(num_rem):
		lst.remove(value)