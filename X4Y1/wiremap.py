#lor=6.52e9
#lor=6.85e9
lor=6.932e9
#loq=4.5e9
#loq=5.7e9
#loq=5.185e9
#loq=4.87e9
#loq=4.9183e9
#loq=4.896e9
#loq=5.44e9
#loq=5.42e9
#loq=5.582e9
#loq=5.5e9
#loq=5.412e9
loq=5.113e9
lofreq={'Q0.rdrv':lor
		,'Q1.rdrv':lor
		,'Q2.rdrv':lor
		,'Q3.rdrv':lor
		,'Q4.rdrv':lor
		,'Q5.rdrv':lor
		,'Q6.rdrv':lor
		,'Q7.rdrv':lor
		,'Q0.qdrv':loq
		,'Q1.qdrv':loq
		,'Q2.qdrv':loq
		,'Q3.qdrv':loq
		,'Q4.qdrv':loq
		,'Q5.qdrv':loq
		,'Q6.qdrv':loq
		,'Q7.qdrv':loq
		,'Q0.read':lor
		,'Q1.read':lor
		,'Q2.read':lor
		,'Q3.read':lor
		,'Q4.read':lor
		,'Q5.read':lor
		,'Q6.read':lor
		,'Q7.read':lor
		,'M0.mark':0
		,'M1.mark':0
		,'M2.mark':0
		,'M3.mark':0
		,'alignment.read':lor
		,'alignment.rdrv':lor
		,'vna.read':lor
		,'vna.rdrv':lor
		}
elemdict={
		'Q0.qdrv':4,'Q0.read':8,'Q0.rdrv':4
 		,'Q1.qdrv':2,'Q1.read':9,'Q1.rdrv':2
		,'Q2.qdrv':3,'Q2.read':10,'Q2.rdrv':3
		,'Q3.qdrv':5,'Q3.read':8,'Q3.rdrv':5
		,'Q4.qdrv':6,'Q4.read':9,'Q4.rdrv':6
		,'Q5.qdrv':1,'Q5.read':10,'Q5.rdrv':1
		,'Q6.qdrv':0,'Q6.read':9,'Q6.rdrv':0
		,'Q7.qdrv':7,'Q7.read':8,'Q7.rdrv':7
		,'M0.mark':12}
destdict={'Q0.qdrv':2,'Q0.read':4,'Q0.rdrv':0
		,'Q1.qdrv':3,'Q1.read':5,'Q1.rdrv':0
		,'Q2.qdrv':1,'Q2.read':6,'Q2.rdrv':0
		,'Q3.qdrv':2,'Q3.read':4,'Q3.rdrv':0
		,'Q4.qdrv':2,'Q4.read':5,'Q4.rdrv':0
		,'Q5.qdrv':2,'Q5.read':6,'Q5.rdrv':0
		,'Q6.qdrv':2,'Q6.read':4,'Q6.rdrv':0
		,'Q7.qdrv':2,'Q7.read':6,'Q7.rdrv':0
		,'vna.read':5,'vna.rdrv':0
		,'alignment.read':5,'alignment.rdrv':0
		,'M0.mark':12}
switchmap={
		'Q0.qdrv':6
		,'Q1.qdrv':None
		,'Q2.qdrv':None
		,'Q3.qdrv':4
		,'Q4.qdrv':2
		,'Q5.qdrv':3
		,'Q6.qdrv':1
		,'Q7.qdrv':5
		,'Q0.rdrv':None
		,'Q1.rdrv':None
		,'Q2.rdrv':None
		,'Q3.rdrv':None
		,'Q4.rdrv':None
		,'Q5.rdrv':None
		,'Q6.rdrv':None
		,'Q7.rdrv':None
		,'Q0.read':None
		,'Q1.read':None
		,'Q2.read':None
		,'Q3.read':None
		,'Q4.read':None
		,'Q5.read':None
		,'Q6.read':None
		,'Q7.read':None
		,'alignment.read':None
		,'alignment.rdrv':None
		,'vna.read':None
		,'vna.rdrv':None
		}
ttydev={"qdrvswitch":{"deviceid":"switch8","hostname":"192.168.1.26","default":0}
		,"rdrvvat":{"deviceid":"attn1","hostname":"192.168.1.26","default":2}
        ,"qdrvlo":{"deviceid":"a4spi_03","hostname":"192.168.1.26","default":{"chan":3,"freq":loq}}
        #,"qdrvlo":{"deviceid":"a4spi_03","hostname":"192.168.1.26","default":{"chan":3,"freq":4.87e9}}
        #,"qdrvlo":{"deviceid":"a4spi_03","hostname":"192.168.1.26","default":{"chan":3,"freq":5.5e9}}
#        ,"readlo":{"deviceid":"a4spi_03","hostname":"192.168.1.26","default":{"chan":1,"freq":6.52e9}}
#,"readlo":{"deviceid":"a4spi_03","hostname":"192.168.1.26","default":{"chan":1,"freq":6.85e9}}
        ,"readlo":{"deviceid":"a4spi_03","hostname":"192.168.1.26","default":{"chan":1,"freq":lor}}
		}
