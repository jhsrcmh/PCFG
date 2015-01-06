##PCFG Trainer and Parser

* Core algorithm 

    *  The CYK Algorithm
    *  Inside-Outside algorithm
    *  Treebank

* Trainer
    *  Input

	    ```python
		 a = '(S(NP(DT the)(NN boy))(VP(VP(VBD saw)(NP(DT a)(NN girl)))(PP(IN with)(NP(DT a)(NN telescope)))))'
	     b = '(S(NP(DT the)(NN girl))(VP(VBD saw)(NP(NP(DT a)(NN boy))(PP(IN with)(NP(DT a)(NN telescope)))'
		```

    *  Training

    	```python
	   material = [a, b]
	   trainer = PCFGTrainer('model.bin')
	   trainer.train(material)
		```

    *  Output

   		 ```python
		VP#VP PP#  0.333333333333 
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
		VBD#saw#  1.0
		```

* Parser

    *  Input

	    ```python
		 s = 'a boy with a telescope saw a girl'
		```

    *  Parsering

    	```python
	    parser = PCFGParser('model.bin') 
	    parser.writeOutResult(s, '2.out')
		```

    *  Output

   		 ```python
   		 #antomate syntax tagged
		(S (NP (NP (DT a) (NN boy)) (PP (IN with) (NP (DT a) (NN telescope)))) (VP (VBD saw) (NP (DT a) (NN girl))))

		#maximium value
		0.000658161979833

		#span value
		PP # 3 # 5 # 0.380952380952 # 0.0552856063059
		NP # 1 # 5 # 0.0414642047294 # 0.507936507937
		NN # 2 # 5 # 0.0 # 0.580498866214
		DT # 1 # 4 # 0.0 # 0.290249433106
		NP # 7 # 8 # 0.380952380952 # 0.0552856063059
		NP # 4 # 5 # 0.380952380952 # 0.0552856063059
		S # 1 # 8 # 0.0210611833546 # 1
		DT # 7 # 7 # 0.666666666667 # 0.0315917750319
		NP # 1 # 2 # 0.380952380952 # 0.0552856063059
		VP # 6 # 8 # 0.507936507937 # 0.0414642047294
		VBD # 6 # 6 # 1.0 # 0.0210611833546
		VP # 3 # 8 # 0.0 # 0.380952380952
		IN # 3 # 3 # 1.0 # 0.0210611833546
		DT # 4 # 4 # 0.666666666667 # 0.0315917750319
		VBD # 3 # 6 # 0.0 # 0.193499622071
		S # 4 # 8 # 0.193499622071 # 0.0
		DT # 1 # 1 # 0.666666666667 # 0.0315917750319
		```