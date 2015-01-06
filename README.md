###PCFG Trainer and Parser
1. Trainer

  Input:
	   a = '(S(NP(DT the)(NN boy))(VP(VP(VBD saw)(NP(DT a)(NN girl)))(PP(IN with)(NP(DT a)(NN telescope)))))'
	   b = '(S(NP(DT the)(NN girl))(VP(VBD saw)(NP(NP(DT a)(NN boy))(PP(IN with)(NP(DT a)(NN telescope)))
  Training:
	   material = [a, b]
	   trainer = PCFGTrainer('model.bin')
	   trainer.train(material)
  Output: model.bin
'''   	VP#VP PP#  0.333333333333 
	VP#VBD NP#  0.666666666667 
	DT#a#  0.666666666667 
	S#NP VP#  1.0 
	DT#the#  0.333333333333 
	NP#DT NN#  0.857142857143 
	PP#IN NP#  1.0 
	NN#girl#  0.333333333333 
	IN#with#  1.0 
	NN#telescope#  0.333333333333 
	NP#NP PP#  0.142857142857 
	NN#boy#  0.333333333333 
	VBD#saw#  1.0 '''