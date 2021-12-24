#chanmapqubit={'Q0.rdrv':0
#		,'Q1.rdrv':0
#		,'Q2.rdrv':0
#		,'Q3.rdrv':0
#		,'Q4.rdrv':0
#		,'Q5.rdrv':0
#		,'Q6.rdrv':0
#		,'Q7.rdrv':0
#		,'Q5.qdrv':3
#		,'Q4.qdrv':2
#		,'Q3.qdrv':2
#		,'Q0.qdrv':2
#		,'Q1.qdrv':2
#		,'Q2.qdrv':2
#		,'Q6.qdrv':2
#		,'Q7.qdrv':1
#		,'Q0.read':4
#		,'Q1.read':5
#		,'Q2.read':6
#		,'Q3.read':4
#		,'Q4.read':5
#		,'Q5.read':6
#		,'Q6.read':4
#		,'Q7.read':5
#		,'M0.mark':13
#		,'M1.mark':14
#		,'M2.mark':15
#		,'M3.mark':16
#		}
ttydev={"qdrvlo":{"deviceid":"a4spi_02","hostname":"192.168.1.24","default":{"chan":3,"freq":5.5e9}}
        ,"readlo":{"deviceid":"a4spi_02","hostname":"192.168.1.24","default":{"chan":1,"freq":6.52e9}}
		,"readvat":{"deviceid":"attn3","hostname":"192.168.1.24","default":10}
        #,"readlo":{"deviceid":"multifreqlo_v1","hostname":"192.168.1.24","default":{"chan":2,"freq":6.52e9}}
		}
lor=6.52e9
#lor=6.52e9
loq=5.5e9
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
		,'alignment.read':lor
		,'alignment.rdrv':lor
		,'vna.read':lor
		,'vna.rdrv':lor
		,'M0.mark':0
		,'M1.mark':0
		,'M2.mark':0
		,'M3.mark':0
		,'alignment.read':lor
		,'alignment.rdrv':lor
		,'vna.read':lor
		,'vna.rdrv':lor
		}
#dacelementsdest=['Q0.rdrv'
#		,'Q1.rdrv'
#		,'Q2.rdrv'
#		,'Q3.rdrv'
#		,'Q4.rdrv'
#		,'Q5.rdrv'
#		,'Q6.rdrv'
#		,'Q7.rdrv'
#		,'Q0.qdrv'
#		,'Q1.qdrv'
#		,'Q2.qdrv'
#		,'Q3.qdrv'
#		,'Q4.qdrv'
#		,'Q5.qdrv'
#		,'Q6.qdrv'
#		,'Q7.qdrv'
#		]
elemdict={'Q0.qdrv':0,'Q0.read':8,'Q0.rdrv':0
		,'Q1.qdrv':1,'Q1.read':8,'Q1.rdrv':1
		,'Q2.qdrv':2,'Q2.read':8,'Q2.rdrv':2
		,'Q3.qdrv':3,'Q3.read':8,'Q3.rdrv':3
		,'Q4.qdrv':4,'Q4.read':8,'Q4.rdrv':4
		,'Q5.qdrv':5,'Q5.read':8,'Q5.rdrv':5
		,'Q6.qdrv':6,'Q6.read':8,'Q6.rdrv':6
		,'Q7.qdrv':7,'Q7.read':8,'Q7.rdrv':7
		,'M0.mark':12}
destdict={'Q0.qdrv':1,'Q0.read':4,'Q0.rdrv':0
		,'Q1.qdrv':1,'Q1.read':4,'Q1.rdrv':0
		,'Q2.qdrv':1,'Q2.read':4,'Q2.rdrv':0
		,'Q3.qdrv':1,'Q3.read':4,'Q3.rdrv':0
		,'Q4.qdrv':1,'Q4.read':4,'Q4.rdrv':0
		,'Q5.qdrv':3,'Q5.read':5,'Q5.rdrv':0
		,'Q6.qdrv':2,'Q6.read':6,'Q6.rdrv':0
		,'Q7.qdrv':1,'Q7.read':4,'Q7.rdrv':0
		,'vna.read':5,'vna.rdrv':0
		,'alignment.read':5,'alignment.rdrv':0
		,'M0.mark':12}
