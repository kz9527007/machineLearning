# -*- coding: utf-8 -*-
import sys
spanish = ['el','la','de','que','y','a','en','un','ser','se','no','haber','por','con','su','para','como','estar','tener','le','lo','lo','todo','pero','más','hacer','o','poder','decir','este','ir','otro','ese','la','si','me','ya','ver','porque','dar','cuando','él','muy','sin','vez','mucho','saber','qué','sobre','mi','alguno','mismo','yo','también','hasta','año','dos','querer','entre','así','primero','desde','grande','eso','ni','nos','llegar','pasar','tiempo','ella','sí','día','uno','bien','poco','deber','entonces','poner','cosa','tanto','hombre','parecer','nuestro','tan','donde','ahora','parte','después','vida','quedar','siempre','creer','hablar','llevar','dejar','nada','cada','seguir','menos','nuevo','encontrar']
german = ['der','die','das','und','sein','in','ein','zu','haben','ich','werden','sie','von','nicht','mit','es','sich','auch','auf','für','an','er','so','dass','können','dies','als','ihr','ja','wie','bei','oder','wir','aber','dann','man','da','sein','noch','nach','was','also','aus','all','wenn','nur','müssen','sagen','um','über','machen','kein','Jahr das','du','mein','schon','vor','durch','geben','mehr','andere','anderer','anderes','viel','kommen','jetzt','sollen','mir','wollen','ganz','mich','immer','gehen','sehr','hier','doch','bis','groß','wieder','Mal das','zwei','gut','wissen','neu','sehen','lassen','uns','weil','unter','denn','stehen','jede','jeder','jedes','Beispiel','Zeit','die','erste','erster','erstes','ihm','ihn','wo','lang','eigentlich','damit','selbst unser','oben']
english = ['the','be','to','of','and','a','in','that','have','I','it','for','not','on','with','he','as','you','do','at','this','but','his','by','from','they','we','say','her','she','or','an','will','my','one','all','would','there','their','what','so','up','out','if','about','who','get','which','go','me','when','make','can','like','time','no','just','him','know','take','people','into','year','your','good','some','could','them','see','other','than','then','now','look','only','come','its','over','think','also','back','after','use','two','how','our','work','first','well','way','even','new','want','because','any','these','give','day','most','us']
french = ['le','de','un','à','être','et','en','avoir','que','pour','dans','ce','il','qui','ne','sur','se','pas','plus','pouvoir','par','je','avec','tout','faire','son','mettre','autre','on','mais','nous','comme','ou','si','leur','y','dire','elle','devoir','avant','deux','même','prendre','aussi','celui','donner','bien','où','fois','vous','encore','nouveau','aller','cela','entre','premier','vouloir','déjà','grand','mon','me','moins','aucun','lui','temps','très','savoir','falloir','voir','quelque','sans','raison','notre','dont','non','an','monde','jour','monsieur','demander','alors','après','trouver','personne','rendre','part','dernier','venir','pendant','passer','peu','lequel','suite','bon','comprendre','depuis','point','ainsi','heure','rester']

def detect(text):
	en, ge, sp, fr = 0, 0, 0, 0
	temp = text.split(' ')
	for word in temp:
		if word in spanish:
			sp += 1
		if word in german:
			ge += 1
		if word in english:
			en += 1
		if word in french:
			fr += 1
	maximum = max([sp,ge,en,fr])
	output = ['Spanish','German','English','French']
	return output[[sp,ge,en,fr].index(maximum)]

if __name__ == "__main__":
	text = ''
	for line in sys.stdin:
		text += ' ' + line.lower().replace('.','').replace('\'','').replace(',','').replace('\"','').replace(';','').replace(':','')

	language = detect(text)
	print language