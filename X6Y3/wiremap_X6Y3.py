#chanmapqubit={'Q0.rdrv':0
#		,'Q1.rdrv':0
#		,'Q2.rdrv':0
#		,'Q3.rdrv':0
#		,'Q4.rdrv':0
#		,'Q5.rdrv':0
#		,'Q6.rdrv':0
#		,'Q7.rdrv':0
#		,'Q5.qdrv':2
#		,'Q4.qdrv':2
#		,'Q3.qdrv':2
#		,'Q0.qdrv':2
#		,'Q1.qdrv':3
#		,'Q2.qdrv':1
#		,'Q6.qdrv':2
#		,'Q7.qdrv':2
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
lor=6.52e9
loq=5.41e9
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
#lo0elementsdest=['Q0.read','Q3.read','Q6.read']
#lo1elementsdest=['Q1.read','Q4.read','Q7.read']
#lo2elementsdest=['Q2.read','Q5.read']
#digielem0dest=['M0.mark']
#digielem1dest=['M1.mark']
#digielem2dest=['M2.mark']
#digielem3dest=['M3.mark']
#gatesall=['M0mark'
#		,'Q0X90','Q0read'
#		,'Q1X90','Q1read'
#		,'Q2X90','Q2read'
#		,'Q3X90','Q3read'
#		,'Q4X90','Q4read'
#		,'Q5X90','Q5read'
#		,'Q6X90','Q6read'
#		,'Q7X90','Q7read'
#		,'Q0Q1CNOT'
#		,'Q1Q2CNOT'
#		,'Q3Q2CNOT'
#		,'Q4Q3CNOT'
#		,'Q5Q4CNOT'
#		,'Q6Q5CNOT'
#		,'Q6Q7CNOT'
#		,'Q7Q0CNOT']
elemdict={
 		 'Q1.qdrv':0,'Q1.read':8,'Q1.rdrv':0
		,'Q2.qdrv':1,'Q2.read':9,'Q2.rdrv':1
		,'Q0.qdrv':2,'Q0.read':10,'Q0.rdrv':2
		,'Q3.qdrv':2,'Q3.read':10,'Q3.rdrv':2
		,'Q4.qdrv':2,'Q4.read':10,'Q4.rdrv':2
		,'Q5.qdrv':2,'Q5.read':10,'Q5.rdrv':2
		,'Q6.qdrv':2,'Q6.read':10,'Q6.rdrv':2
		,'Q7.qdrv':2,'Q7.read':10,'Q7.rdrv':2
		,'M0.mark':12}
destdict={'Q0.qdrv':2,'Q0.read':4,'Q0.rdrv':0
		,'Q1.qdrv':3,'Q1.read':5,'Q1.rdrv':0
		,'Q2.qdrv':1,'Q2.read':6,'Q2.rdrv':0
		,'Q3.qdrv':2,'Q3.read':4,'Q3.rdrv':0
		,'Q4.qdrv':2,'Q4.read':5,'Q4.rdrv':0
		,'Q5.qdrv':2,'Q5.read':6,'Q5.rdrv':0
		,'Q6.qdrv':2,'Q6.read':4,'Q6.rdrv':0
		,'Q7.qdrv':2,'Q7.read':5,'Q7.rdrv':0
		,'vna.read':5,'vna.rdrv':0
		,'alignment.read':5,'alignment.rdrv':0
		,'M0.mark':12}
#patchlistall={'Q0.rdrv':8e-9,'Q0.read':8e-9,'Q0.qdrv':8e-9
#		,'Q2.rdrv':0,'Q2.read':0,'Q2.qdrv':0
#		,'Q1.rdrv':8e-9,'Q1.read':8e-9,'Q1.qdrv':8e-9
#		,'Q3.rdrv':0,'Q3.read':0,'Q3.qdrv':0
#		,'Q4.rdrv':8e-9,'Q4.read':8e-9,'Q4.qdrv':8e-9
#		,'Q5.rdrv':0,'Q5.read':0,'Q5.qdrv':0
#		,'Q6.rdrv':8e-9,'Q6.read':8e-9,'Q6.qdrv':8e-9
#		,'Q7.rdrv':0,'Q7.read':0,'Q7.qdrv':0
#		,'M0.mark':0}
#patchmaxlistall={'Q0.rdrv':100,'Q0.read':100,'Q0.qdrv':100
#		,'Q1.rdrv':100,'Q1.read':100,'Q1.qdrv':100
#		,'Q2.rdrv':100,'Q2.read':100,'Q2.qdrv':100
#		,'Q3.rdrv':100,'Q3.read':100,'Q3.qdrv':100
#		,'Q4.rdrv':100,'Q4.read':100,'Q4.qdrv':100
#		,'Q5.rdrv':100,'Q5.read':100,'Q5.qdrv':100
#		,'Q6.rdrv':100,'Q6.read':100,'Q6.qdrv':100
#		,'Q7.rdrv':100,'Q7.read':100,'Q7.qdrv':100
#		,'M0.mark':100}
#patchdict=patchmaxlistall
#elemdict=elementlistall
#destdict=destlistall
#
#gates=[
#'Q2X90'
#,'Q1X90'
#,'Q2read'
#,'Q1read'
##,'Q5Q4CNOT'
##,'Q5Q6CNOT'
##,'Q1read'
##,'Q4X180'
##,'Q5X180'
##,'Q6X180'
##,'Q1X90'
##,'Q2X90'
##,'Q3X90'
##,'Q0X90'
##,'Q7X90'
#]
switchmap={
		'Q0.qdrv':6
		,'Q1.qdrv':None
		,'Q2.qdrv':None
		,'Q3.qdrv':3
		,'Q4.qdrv':5
		,'Q5.qdrv':2
		,'Q6.qdrv':1
		,'Q7.qdrv':4
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
ttydev={"qdrvswitch":{"deviceid":"switch8","hostname":"qubic","default":0}
		,"rdrvvat":{"deviceid":"attn1","hostname":"qubic2","default":8}
		}
