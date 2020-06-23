# *Finance-Word-Embedding-Framework*
This Word Embedding Framework is tailor made for feature extraction from textual data which is related to finance, banking, business.
</br>
</br>
</br>
### Word Embedding:
  It is the dense vector representation of a word in a low dimension (e.g.-100,200) vector space. In this vector space the words which 
  are similar in meaning or usage are positioned closer to each other compared to dissimilar words. The measure of closeness is cosine
  similarity.
</br>
</br>  
### Corpus:  
  Some of the prominent text books in the field of finance were used to form the corpus. Some of them are mentioned below:
   * The Intelligent Investor
   * Investment Banking
   * Principles of Corporate Finance
   * Introduction to Structured Finance
   * Investment Leadership and Portfolio Management
</br>
</br>
  
### Pre-Processing of the Text Corpus:
* Removal of Named Entities.
* Removal of non-english words.
* Lower-casing all the words.
* Removing stop-words.
* Removing numbers and punctuations.
</br>
</br>


### Glove Model:
  GloVe is a word vector technique it is an abbreviation which stands for Global Vectors. The advantage of GloVe is that, unlike Word2vec,   GloVe does not rely just on local statistics (local context information of words), but incorporates global statistics (word co-  
  occurrence) to obtain word vectors.
  It efficiently leverages statistical information by training only on the non-zero elements in a word co-occurrence matrix, rather than on   the entire sparse matrix or on individual context windows in a large corpus.
  
 * **Co-Occurence Matrix**:
     A co-occurrence matrix is a term-term matrix and will have unique words in rows and columns . The purpose of this matrix is to 
     present the number of time each word  appears in the same context as each word in columns.
 * **Loss Function**: 
     <img src="https://bit.ly/2Ctq97b" align="center" border="0" alt=" \sum_{i,j=1}^V  f(x_{i,j})[w^T_i \tilde{w}_j + b_i +\tilde{b}_j - log(x_{i,j})]^2" width="306" height="56" />

   * <img src="http://www.sciweavers.org/tex2img.php?eq=w_i&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0" align="center" border="0" alt="w_i" width="24" height="15" />= word-embedding of ith  word in row of co-occurrence matrix (focus word)

   * <img src="https://bit.ly/2Yps0T1" align="center" border="0" alt=" \tilde{w}_j " width="24" height="21" />= word-embedding of jth  word in column of co-occurrence matrix (context word)

   * <img src="https://bit.ly/3fR4Evz" align="center" border="0" alt=" b_i" width="19" height="18" />= Bias term for ith focus word

   * <img src="http://www.sciweavers.org/tex2img.php?eq=%5Ctilde%7Bb%7D_j&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0" align="center" border="0" alt="\tilde{b}_j" width="19" height="25" />= Bias term for jth context word.
   * <img src="http://www.sciweavers.org/tex2img.php?eq=%20x_%7Bi%2Cj%7D&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0" align="center" border="0" alt=" x_{i,j}" width="26" height="18" />= (i,j)th  element of the co-occurrence matrix.
   * <img src="https://bit.ly/2NklIOk" align="center" border="0" alt="f(X_{i,j})" width="50" height="21" /> =<img src="http://www.sciweavers.org/tex2img.php?eq=min%281%2C%7BX_%7Bi%2Cj%7D%2F%28%7B%5Cmax_%7B%5Cforall%20%7Bi%2Cj%7D%7D%20X_%7Bi%2Cj%7D%7D%29%5E%7B3%2F4%7D%29%20&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0" align="center" border="0" alt="min(1,{X_{i,j}/({\max_{\forall {i,j}} X_{i,j}})^{3/4}) " width="203" height="26" />     a.k.a weighing function
   * **V**        = size of the vocabulary or simply number of unique words in the corpus


* **Working**: 
  The word embeddings are obtained by minimising the loss function through gradient descent.Since, the embeddings are a solution
  obtained through gradient descent they will always be slightly different each time we obtain them for the same set of hyper-parameters
  as every-time the solution we obtain will be sub-optimal.
  
</br>
</br>

### Optimal set of Hyper-parameters for Glove model:
  For our use-case the set of hyper-parameters turns out to be as follows.
   * Window=3
   * Number of dimensions=100
   * Learning rate = 0.01
   * Number of epochs=10

