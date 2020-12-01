# pyCausalFS：A Python Library of Causality-based Feature Selection for Causal Structure Learning and Classification

## Overview

The pyCausalFS library provides access to a wide range of well-established and state-of-the-art causality-based feature selection approaches. The library is designed to facilitate the development of new algorithms in this research area and make it easier to compare new methods and existing ones available.  
  	
The pyCausalFS library implements 30 representative causality-based feature selection methods. Specifically, it consists of 25 methods using conditional independence tests (16 single MB learning algorithms, 3 multiple MB learning algorithms, and 6 PC learning algorithms), and 5 score-based approaches. 
  
1）	Constraint-based MB learning methods:

	GSMB, IAMB, IAMBnPC, Inter-IAMB, Fast-IAMB, Inter-IAMBnPC, LRH, BAMB, FBEDk, MMMB, PCMB, HITON-MB,
	Semi-HITON-MB, IPCMB, STMB, MBOR

2）	Multiple MB learning methods:

	KIAMB, TIE*(TIE and TIE_p)

3）	Constraint-based PC learning methods:

	PC-simple, MBtoPC, HITON-PC, Semi-HITON-PC, GetPC, MMPC

4）	score-based MB learning methods:

	SLL, S^2TMB, S^2TMB_p

5）	score-based PC learning methods:

	SLL-PC, S^2TMB-PC

Furthermore, using the pyCausalFS library, users can easily generate different local structure learning methods and local-to-global structure learning methods, which includes 3 local BN structure learning algorithms and three local-to-global BN learning algorithms.

6）	local BN structure learning algorithms:

	PCD-by-PCD, MB-by-MB, CMB

7）	local-to-global BN learning algorithms:

	MMHC, GSBN, MBGSL
    
All implementation details please read the manual documentation.