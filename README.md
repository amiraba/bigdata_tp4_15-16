# TP4 - Big Data - Cassandra - CQL - Pycassa

## Partie 1 - Cassandra - Installation et familiarisation avec CQL

```
apt-get install cassandra
cassandra
cqlsh
service cassandra stop #Pour arrêter le service
```

![screenshot from 2017-04-22 19-45-16](https://cloud.githubusercontent.com/assets/23452983/25308958/33dbce4a-27b8-11e7-872a-20a9ecf43291.png)

Un keyspace est un regroupement de famille de colonnes. Il s'agit d'une sorte de schéma si on compare au monde des bases de données relationnelles.

![screenshot from 2017-04-22 19-44-58](https://cloud.githubusercontent.com/assets/23452983/25308956/2ae62542-27b8-11e7-91fa-63aadbce4f4c.png)

![screenshot from 2017-04-22 19-54-41](https://cloud.githubusercontent.com/assets/23452983/25308961/37b8f2cc-27b8-11e7-802f-6efd155af2af.png)

### Collections

#### Sets
![screenshot from 2017-04-22 20-00-20](https://cloud.githubusercontent.com/assets/23452983/25308966/43f4fcb6-27b8-11e7-9fdb-cf0b4de42e5a.png)

#### Listes
![screenshot from 2017-04-22 20-02-01](https://cloud.githubusercontent.com/assets/23452983/25308968/47b5ccc2-27b8-11e7-874c-0261bb3f33f8.png)

#### Maps
![screenshot from 2017-04-22 20-08-37](https://cloud.githubusercontent.com/assets/23452983/25308970/4e8adf1a-27b8-11e7-95af-5819f428349d.png)

## Partie 2 - Pycassa - Thrift

Afin d'effectuer le lien de Python avec la base cassandra, certains prérequis doivent êtres présents lors de l'installation:
- Cassandra doit être active sur le port 9160 à travers `nodetool enablethrift` après `apt-get install thrift`. Thrift est indispensable car c'est l'IDL qui permet la portabilité de l'accès à Cassandra de manière indépendante du langage utilisé afin de faciliter sa communication avec d'autres composants logiciels, notamment du code Python.

![screenshot from 2017-04-22 22-43-36](https://cloud.githubusercontent.com/assets/23452983/25308981/7441546e-27b8-11e7-85e9-a0a4f12c4354.png)
- Installation classique de Pycassa.
```
git clone git://github.com/pycassa/pycassa.git
$ cd pycassa/
$ sudo python setup.py install
```
- N'oublions pas d'inclure `WITH COMPACT STORAGE` lors de la création de notre famille de colonnes sur Cassandra.

![screenshot from 2017-04-22 22-41-43](https://cloud.githubusercontent.com/assets/23452983/25308972/5621df8a-27b8-11e7-94a0-416840658ca0.png)

- Tests variés:

![screenshot from 2017-04-22 22-43-09](https://cloud.githubusercontent.com/assets/23452983/25308978/63019cf4-27b8-11e7-821f-332c0ed7f134.png)

![screenshot from 2017-04-22 22-44-20](https://cloud.githubusercontent.com/assets/23452983/25308986/9f9a42a6-27b8-11e7-8a4c-6563d7e84f20.png)

![screenshot from 2017-04-22 22-46-08](https://cloud.githubusercontent.com/assets/23452983/25308987/a4e8a7de-27b8-11e7-9e33-cf41ff42f84d.png)

![screenshot from 2017-04-22 22-48-15](https://cloud.githubusercontent.com/assets/23452983/25308988/a95c3fe2-27b8-11e7-88d6-b5fab6266f87.png)

![screenshot from 2017-04-22 22-53-18](https://cloud.githubusercontent.com/assets/23452983/25308989/abee12a8-27b8-11e7-824e-7366d0dbd446.png)

![screenshot from 2017-04-22 22-53-53](https://cloud.githubusercontent.com/assets/23452983/25308990/afebb11c-27b8-11e7-858f-fd64437c39a0.png)

## Partie 3 - Objectif du TP

#### Côté Cassandra

![screenshot from 2017-04-22 23-40-18](https://cloud.githubusercontent.com/assets/23452983/25308992/b44607bc-27b8-11e7-8cf4-3931bc1939e9.png)

#### Côté Pycassa

`find bible -type f -name "*.txt" -print0 | xargs -0 cat | sed "s/^[0-9 ]*//" | python populate.py`
![screenshot from 2017-04-23 00-39-20](https://cloud.githubusercontent.com/assets/23452983/25309160/5f8a9c1a-27bd-11e7-8b91-8fde1f8f7b1c.png)

![screenshot from 2017-04-22 23-45-22](https://cloud.githubusercontent.com/assets/23452983/25308998/bf090154-27b8-11e7-8f5c-847af2d02eeb.png)

# Conclusion

Grâce à ce TP, nous avons pu déceler le fonctionnement d'une des bases de données orientées colonnes les plus populaires "Cassandra". On a pu voir de près non seulement sa structure mais aussi pourquoi elle est qualifiée de "la plus rapide". En effet, l'ajout des milliers de versets de la bible n'a pris que 4 secondes, ce qui est considérablement plus optimisé par rapport à d'autres bases de données.

Certes, si on devait modifier les colonnes, on aurait procédé par un décalage lourd de tout le volume de données. Mais , dans notre cas, et conformément au usecase demandé (Remplissage de la base par des versets), elle s'avère la plus performante.
