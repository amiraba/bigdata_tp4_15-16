#!/usr/bin/python
import sys

#Connexion à cassandra
import pycassa
pool=pycassa.ConnectionPool(keyspace='wordcount', server_list=['127.0.0.1:9160'])
bible = pycassa.ColumnFamily(pool, 'bible')

theId=0

for line in sys.stdin:
	data = line.strip().split(" ",1) #On tronque le numéro du verset
	number, verset =data
	#print "{0}\n".format(verset)
	bible.insert(theId, {'line': verset })  #On insère dans la famille de colonnes bible notre nouveau verset avec un l'identifiant automatiquement incrémenté
	theId= theId + 1


