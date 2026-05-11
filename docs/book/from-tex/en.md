# Foreword {#foreword .unnumbered}

I am happy to see Kenji Hiranabe's pictures of matrix operations in linear algebra !
The pictures are an excellent way to show the algebra. We can think of matrix
multiplications by row $\bm{\cdot}$ column dot products, but that is not all -- it is "linear combinations\"
and "rank 1 matrices\" that complete the algebra and the art.
I am very grateful to see the books in Japanese translation
and the ideas in Kenji's pictures.

::: flushright
-- Gilbert Strang\
Professor of Mathematics at MIT
:::

# Viewing a Matrix -- 4 Ways

A matrix ($m \times n$) can be seen as $1$ matrix, $mn$ numbers, $n$ columns and $m$ rows.

<figure data-latex-placement="H">
<p><embed src="ViewingMatrix-4Ways.eps" /><br />
</p>
<figcaption>Viewing a Matrix in 4 Ways</figcaption>
</figure>

$$\begin{equation*}
  A= \begin{bmatrix}
    a_{11} & a_{12}\\
    a_{21} & a_{22}\\
    a_{31} & a_{32}
  \end{bmatrix}
  =
  \begin{bmatrix}
    | & |\\
    \bm{a_1} & \bm{a_2}\\
    | & |
  \end{bmatrix}
  =
  \begin{bmatrix}
    - \bm{a_1^*} -\\
    - \bm{a_2^*} -\\
    - \bm{a_3^*} -
  \end{bmatrix}
\end{equation*}$$\
Here, the column vectors are in bold as $\bm{a_1}$.
Row vectors include $\bm{*}$ as in $\bm{a_1^*}$.
Transposed vectors and matrices are indicated by $\mathrm{T}$ as
in $\bm{a}^{\mathrm{T}}$ and $A^{\mathrm{T}}$.

# Vector times Vector -- 2 Ways

Hereafter I point to specific sections of "Linear Algebra for Everyone\"
and present graphics which illustrate the concepts with short names
in gray circles.

- Sec. 1.1 (p.2) Linear combination and dot products

- Sec. 1.3 (p.25) Matrix of Rank One

- Sec. 1.4 (p.29) Row way and column way

<figure data-latex-placement="H">
<embed src="VectorTimesVector.eps" />
<figcaption>Vector times Vector - (v1), (v2)</figcaption>
</figure>

(v1) is a elementary operation of two vectors, but (v2) multiplies the column to the row
and produce a rank 1 matrix. Knowing this outer product (v2) is the key for the later sections.

# Matrix times Vector -- 2 Ways

A matrix times a vector creates a vector of three dot products (Mv1)
as well as a linear combination (Mv2) of the column vectors of $A$.

- Sec. 1.1 (p.3) Linear combinations

- Sec. 1.3 (p.21) Matrices and Column Spaces

<figure data-latex-placement="H">
<embed src="MatrixTimesVector.eps" />
<figcaption>Matrix times Vector - (Mv1), (Mv2)</figcaption>
</figure>

At first, you learn (Mv1). But when you get used to viewing it as (Mv2),
you can understand $A\bm{x}$ as a linear combination of the columns of $A$.
Those products fill the column space of $A$ denoted as $\mathbf{C}(A)$.
The solution space of $A\bm{x}=\bm{0}$ is the nullspace of $A$ denoted as $\mathbf{N}(A)$.
To understand the nullspace, let the right-hand side of (Mv1) be $\bm{0}$
and see all the dot products are zero.

Also, (vM1) and (vM2) shows the same patterns for a row vector times a matrix.

<figure data-latex-placement="H">
<embed src="VectorTimesMatrix.eps" />
<figcaption>Vector times Matrix - (vM1), (vM2)</figcaption>
</figure>

The products fill the row space of $A$ denoted as $\mathbf{C}(A^{\mathrm{T}})$.
The solution space of $yA=0$ is the left-nullspace of $A$, denoted as $\mathbf{N}(A^{\mathrm{T}})$.

The four subspaces consists of $\mathbf{N}(A)$ + $\mathbf{C}(A^{\mathrm{T}})$
(which are perpendicular to each other) in $\mathbb{R}^n$ and
$\mathbf{N}(A^{\mathrm{T}})$ + $\mathbf{C}(A)$ in $\mathbb{R}^m$
(which are perpendicular to each other).

- Sec. 3.5 (p.124) Dimensions of the Four Subspaces

<figure data-latex-placement="H">
<embed src="4-Subspaces.eps" style="width:8cm" />
<figcaption>The Four Subspaces</figcaption>
</figure>

See $A=CR$ (Sec 6.1) for the rank $r$.

# Matrix times Matrix -- 4 Ways

"Matrix times Vector\" naturally extends to "Matrix times Matrix\".

- Sec. 1.4 (p.35) Four Ways to Multiply $\bm{AB=C}$

- Also see the back cover of the book

<figure data-latex-placement="H">
<embed src="MatrixTimesMatrix.eps" />
<figcaption>Matrix times Matrix - (MM1), (MM2), (MM3), (MM4)</figcaption>
</figure>

# Practical Patterns

Here, I show some practical patterns which allow you to capture
the coming factorizations more intuitively.

<figure data-latex-placement="H">
<embed src="Pattern12.eps" />
<figcaption>Pattern 1, 2 - (P1), (P1)</figcaption>
</figure>

Pattern 1 is a combination of (MM2) and (Mv2).
Pattern 2 is an extention of (MM3). Note that Pattern 1 is a column operation (multiplying a matrix from right),
whereas Pattern 2 is a row operation (multiplying a matrix from left).

<figure data-latex-placement="H">
<embed src="Pattern11-22.eps" />
<figcaption>Pattern 1<span class="math inline"><sup>′</sup></span>, 2<span class="math inline"><sup>′</sup></span> - (P1<span class="math inline"><sup>′</sup></span>), (P2<span class="math inline"><sup>′</sup></span>)</figcaption>
</figure>

(P1$^\prime$) multipies the diagonal numbers to the columns of the matrix,
whereas (P2$^\prime$) multipies the diagonal numbers to the row of the matrx.
Both are variants of (P1) and (P2).

<figure data-latex-placement="H">
<embed src="Pattern3.eps" />
<figcaption>Pattern 3 - (P3)</figcaption>
</figure>

This pattern appears when you solve differential equations and recurrence equations:

- Sec. 6 (p.201) Eigenvalues and Eigenvectors

- Sec. 6.4 (p.243) Systems of Differential Equations

$$\begin{align*}
  \frac{d \bm{u}(t) }{dt} &= A \bm{u}(t), \quad \bm{u}(0)=\bm{u}_0\\
  \bm{u}_{n+1} &= A \bm{u}_n, \quad \bm{u_0} = \bm{u}_0
\end{align*}$$

In both cases, the solutions are expressed with
eigenvalues ($\lambda_1, \lambda_2, \lambda_3$),
eigenvectors $X=\begin{bmatrix} \bm{x}_1 & \bm{x}_2 & \bm{x}_3 \end{bmatrix}$ of $A$, and
the coefficients $c=\begin{bmatrix} c_1 & c_2 & c_3 \end{bmatrix}^{\mathrm{T}}$
which are the coordinates of the initial condition $\bm{u}(0)=\bm{u}_0$ in terms of
the eigenvectors $X$.

$$\begin{equation*}
  \bm{u}_0 = c_1 \bm{x}_1 + c_2 \bm{x}_2 + c_3 \bm{x}_3
\end{equation*}$$
$$\begin{equation*}
  \bm{c} =
  \begin{bmatrix}
    c_1\\
    c_2\\
    c_3
  \end{bmatrix} = X^{-1} \bm{u}_0
\end{equation*}$$

and the general solution of the two equations are:

$$\begin{align*}
  \bm{u}(t) &= e^{At} \bm{u}_0 = X e^{\Lambda t} X^{-1} \bm{u_0} &= X e^{\Lambda t} \bm{c} &= c_1 e^{\lambda_1 t} \bm{x}_1 + c_2 e^{\lambda_2 t} \bm{x}_2 + c_3 e^{\lambda_3 t} \bm{x}_3\\
  \bm{u}_n &= A^n \bm{u}_0 = X \Lambda^n X^{-1} \bm{u_0} &= X \Lambda^n \bm{c} &= c_1 \lambda_1^n \bm{x}_1 + c_2 \lambda_2^n \bm{x}_2 + c_3 \lambda_3^n \bm{x}_3
\end{align*}$$

See Figure 9: Pattern 3 (P3) above again to get $XDc$.

<figure data-latex-placement="H">
<embed src="Pattern4.eps" />
<figcaption>Pattern 4 - (P4)</figcaption>
</figure>

This pattern (P4) works in both eigenvalue decomposition and singular value decomposition.
Both decompositions are expressed as a product of three matrices with a diagonal matrix in the middle,
and also a sum of rank 1 matrices with the eigenvalue/singular value coefficients.

More details are discussed in the next section.

# The Five Factorizations of a Matrix

- Preface p.vii, The Plan for the Book.

$A=CR, A=LU, A=QR, A=Q \Lambda Q^{\mathrm{T}}, A=U \Sigma V^{\mathrm{T}}$ are
illustrated one by one.

+:----------------------------+:---------------------+:--------------------------------------------------+
| $A=CR$                      | ![image](A_CR.eps)   |   ---------------------------------               |
|                             |                      |   Independent columns in $C$                      |
|                             |                      |   Row echelon form in $R$                         |
|                             |                      |   Leads to column rank = row rank                 |
|                             |                      |   ---------------------------------               |
|                             |                      |                                                   |
|                             |                      |   : The Five Factorization                        |
+-----------------------------+----------------------+---------------------------------------------------+
| $A=LU$                      | ![image](A_LU.eps)   |   --------------------------------------          |
|                             |                      |   $LU$ decomposition from                         |
|                             |                      |   Gaussian elimination                            |
|                             |                      |   (Lower triangular)(Upper triangular)            |
|                             |                      |   --------------------------------------          |
|                             |                      |                                                   |
|                             |                      |   : The Five Factorization                        |
+-----------------------------+----------------------+---------------------------------------------------+
| $A=QR$                      | ![image](A_QR.eps)   |   -----------------------------------             |
|                             |                      |   $QR$ decomposition as                           |
|                             |                      |   Gram-Schmidt orthogonalization                  |
|                             |                      |   Orthogonal $Q$ and triangular $R$               |
|                             |                      |   -----------------------------------             |
|                             |                      |                                                   |
|                             |                      |   : The Five Factorization                        |
+-----------------------------+----------------------+---------------------------------------------------+
| $S=Q\Lambda Q^{\mathrm{T}}$ | ![image](A_QLQT.eps) |   ----------------------------------------------- |
|                             |                      |   Eigenvalue decomposition                        |
|                             |                      |   of a symmetric matrix $S$                       |
|                             |                      |   Eigenvectors in $Q$, eigenvalues in $\Lambda$   |
|                             |                      |   ----------------------------------------------- |
|                             |                      |                                                   |
|                             |                      |   : The Five Factorization                        |
+-----------------------------+----------------------+---------------------------------------------------+
| $A=U\Sigma V^{\mathrm{T}}$  | ![image](A_USVT.eps) |   ------------------------------                  |
|                             |                      |   Singular value decomposition                    |
|                             |                      |   of all matrices $A$                             |
|                             |                      |   Singular values in $\Sigma$                     |
|                             |                      |   ------------------------------                  |
|                             |                      |                                                   |
|                             |                      |   : The Five Factorization                        |
+-----------------------------+----------------------+---------------------------------------------------+

: The Five Factorization

## $\boldsymbol{A=CR}$

- Sec.1.4 Matrix Multiplication and $\bm{A=CR}$ (p.29)

All general rectangular matrices $A$ have the same row rank as the column rank.
This factorization is the most intuitive way to understand this theorem.
$C$ consists of independent columns of $A$, and $R$ is the row reduced echelon form of $A$.
$A=CR$ reduces to $r$ independent columns in $C$ times $r$ independent rows in $R$.

$$\begin{equation*}
  \begin{split}
    A &= CR\\
  \begin{bmatrix}
    1 & 2 & 3 \\
    2 & 3 & 5
  \end{bmatrix}
  & =
  \begin{bmatrix}
    1 & 2 \\
    2 & 3
  \end{bmatrix}
  \begin{bmatrix}
    1 & 0 & 1 \\
    0 & 1 & 1
  \end{bmatrix}
\end{split}
\end{equation*}$$

Procedure: Look at the columns of $A$ from left to right. Keep independent ones,
discard dependent ones which can be created by the former columns.
The column 1 and the column 2 survive, and the column 3 is discarded
because it is expressed as a sum of the former two columns.
To rebuild $A$ by the independent columns 1, 2, you find a row echelon form $R$
appearing in the right.

<figure data-latex-placement="H">
<embed src="CR1.eps" />
<figcaption>Column Rank in <span class="math inline"><em>C</em><em>R</em></span></figcaption>
</figure>

Now you see the column rank is two because there are only two independent columns in $C$
and all the columns of $A$ are linear combinations of the two columns of $C$.

<figure data-latex-placement="H">
<embed src="CR2.eps" />
<figcaption>Row Rank in <span class="math inline"><em>C</em><em>R</em></span></figcaption>
</figure>

And you see the row rank is two because there are only two independent rows in $R$
and all the rows of $A$ are linear combinations of the two rows of $R$.

## $\boldsymbol{A=LU}$

Solving $A\bm{x}=\bm{b}$ via Gaussian elimination can be expressed as an $LU$ factorization.
Usually, you apply elementary row operation matrices ($E$) to $A$ to make upper trianglar $U$.

$$\begin{align*}
  EA &= U\\
  A &= E^{-1}U\\
\text{let} \; L = E^{-1}, \quad  A &= LU
\end{align*}$$

Now solve $A\bm{x}=\bm{b}$ in 2 steps: (1) forward $L\bm{c}=\bm{b}$ and (2) back $U\bm{x}=\bm{c}$.

- Sec.2.3 (p.57) Matrix Computations and $\bm{A=LU}$

Here, we directly calculate $L$ and $U$ from $A$.

$$\begin{equation*}
  A = 
      \begin{bmatrix}
        |\\
        \bm{l}_1\\
        |
      \end{bmatrix}
      \begin{bmatrix}
        -  \bm{u}^*_1  -
      \end{bmatrix}
  +  \begin{bmatrix}
      0 & \begin{matrix} 0 & 0 \end{matrix}\\
      \begin{matrix} 0 \\ 0 \end{matrix} & A_2
    \end{bmatrix}
  = 
  \begin{bmatrix}
    |\\
    \bm{l}_1\\
    |
  \end{bmatrix}
  \begin{bmatrix}
    - \bm{u}^*_1 -
  \end{bmatrix}
  +
  \begin{bmatrix}
    |\\
    \bm{l}_2\\
    |
  \end{bmatrix}
  \begin{bmatrix}
    - \bm{u}^*_2  -
  \end{bmatrix}
  +  \begin{bmatrix}
  0 & 0 & 0\\
  0 & 0 & 0 \\
  0 & 0 & A_3
  \end{bmatrix} = LU
\end{equation*}$$

<figure data-latex-placement="H">
<embed src="LU1.eps" />
<figcaption>Recursive Rank 1 Matrix Peeling from <span class="math inline"><em>A</em></span></figcaption>
</figure>

To find $L$ and $U$, peel off the rank 1 matrix made of
the first row and the first column of $A$.
This leaves $A_2$. Do this recursively and decompose $A$ into the sum of rank 1 matrices.

<figure data-latex-placement="H">
<embed src="LU2.eps" />
<figcaption><span class="math inline"><em>L</em><em>U</em></span> rebuilds <span class="math inline"><em>A</em></span></figcaption>
</figure>

To rebuild $A$ from $L$ times $U$, use column-row multiplication.

## $\boldsymbol{A=QR}$

$A=QR$ changes the columns of $A$ into perpendicular columns of $Q$, keeping $\bm{C}(A) = \bm{C}(Q)$.

- Sec.4.4 Orthogonal matrices and Gram-Schmidt (p.165)

In Gram-Schmidt, the normalized $\bm{a}_1$ is $\bm{q}_1$.
Then $\bm{a}_2$ is adjusted to be perpendicular to $\bm{q}_1$ to create $\bm{q}_2$.
This procedure gives:

$$\begin{align*}
  \bm{q}_1 &= \bm{a}_1/||\bm{a}_1|| \\
  \bm{q}_2 &= \bm{a}_2 - (\bm{q}_1^{\mathrm{T}}\bm{a}_2)\bm{q}_1 , \quad \bm{q}_2 = \bm{q}_2/||\bm{q}_2|| \\
  \bm{q}_3 &= \bm{a}_3 - (\bm{q}_1^{\mathrm{T}}\bm{a}_3)\bm{q}_1 - (\bm{q}_2^{\mathrm{T}}\bm{a}_3)\bm{q}_2, \quad \bm{q}_3 = \bm{q}_3/||\bm{q}_3||
\end{align*}$$

In the reverse direction, letting $r_{ij} = \bm{q}_i^{\mathrm{T}}\bm{a}_j$ and you get:

$$\begin{align*}
  \bm{a}_1 &= r_{11}\bm{q}_1\\
  \bm{a}_2 &= r_{12}\bm{q}_1 + r_{22} \bm{q}_2\\
  \bm{a}_3 &= r_{13}\bm{q}_1 + r_{23} \bm{q}_2 + r_{33} \bm{q}_3
\end{align*}$$

The original $A$ becomes $QR$: orthogonal $Q$ times upper triangular $R$.

$$\begin{gather*}
  A = 
  \begin{bmatrix}
    | & | & |\\
    \bm{q}_1 & \bm{q}_2 & \bm{q}_3\\
    | & | & |
  \end{bmatrix}
  \begin{bmatrix}
    r_{11} & r_{12} & r_{13}\\
           & r_{22} & r_{23}\\
           &        & r_{33}
  \end{bmatrix} = QR\\
  \\
  Q Q^{\mathrm{T}}=Q^{\mathrm{T}}Q = I
\end{gather*}$$

<figure data-latex-placement="H">
<embed src="QR.eps" />
<figcaption><span class="math inline"><em>A</em> = <em>Q</em><em>R</em></span></figcaption>
</figure>

Each column vector of $A$ can be rebuilt from $Q$ and $R$ .

See Pattern 1 (P1) again for the graphic interpretation.

## $\boldsymbol{S=Q \Lambda Q^{\mathrm{T}}}$

All symmetric matrices $S$ must have real eigenvalues and orthogonal eigenvectors.
The eigenvalues are the diagonal elements of $\Lambda$ and the eigenvectors are in $Q$.

- Sec.6.3 (p.227) Symmetric Positive Definite Matrices

$$\begin{align*}
  S = Q \Lambda Q^{\mathrm{T}}
&= \begin{bmatrix}
    | & | & |\\
    \bm{q}_1 & \bm{q}_2 & \bm{q}_3\\
    | & | & |
  \end{bmatrix}
  \begin{bmatrix}
    \lambda_1 \\
           & \lambda_2 & \\
           & & \lambda_3
  \end{bmatrix}
  \begin{bmatrix}
  - \bm{q}_1^{\mathrm{T}}-\\
  - \bm{q}_2^{\mathrm{T}}-\\
  - \bm{q}_3^{\mathrm{T}}-
  \end{bmatrix}\\
  \\
  &=
  \lambda_1 \begin{bmatrix}
    |\\
    \bm{q}_1\\
    |
  \end{bmatrix}
  \begin{bmatrix}
    - \bm{q}_1^{\mathrm{T}}- 
  \end{bmatrix}
  +
  \lambda_2 \begin{bmatrix}
  |\\
  \bm{q}_2\\
  |
  \end{bmatrix}
  \begin{bmatrix}
  - \bm{q}_2^{\mathrm{T}}-
  \end{bmatrix} 
  +
  \lambda_3 \begin{bmatrix}
    |\\
    \bm{q}_3 \\
    |
  \end{bmatrix}
  \begin{bmatrix}
    - \bm{q}_3^{\mathrm{T}}-
  \end{bmatrix} \\
&= \lambda_1 P_1 + \lambda_2 P_2 + \lambda_3 P_3
\end{align*}$$

$$\begin{equation*}
  P_1=\bm{q}_1 \bm{q}_1^{\mathrm{T}}, \quad P_2=\bm{q}_2 \bm{q}_2^{\mathrm{T}}, \quad P_3=\bm{q}_3 \bm{q}_3^{\mathrm{T}}
\end{equation*}$$

<figure data-latex-placement="H">
<embed src="EVD.eps" />
<figcaption><span class="math inline"><em>S</em> = <em>Q</em><em>Λ</em><em>Q</em><sup>T</sup></span></figcaption>
</figure>

A symmetric matrix $S$ is diagonalized into $\Lambda$ by an orthogonal matrix $Q$
and its transpose. And it is broken down into a combination of rank 1 projection matrices $P=qq^{\mathrm{T}}$.
This is the spectral theorem.

Note that Pattern 4 (P4) is working for the decomposition.

$$\begin{gather*}
  S=S^{\mathrm{T}}= \lambda_1 P_1 + \lambda_2 P_2 + \lambda_3 P_3\\
  QQ^{\mathrm{T}}= P_1 + P_2 + P_3 = I \\
  P_1 P_2 = P_2 P_3 = P_3 P_1 = O\\
  P_1^2 =P_1=P_1^{\mathrm{T}}, \quad P_2^2=P_2=P_2^{\mathrm{T}}, \quad P_3^2=P_3=P_3^{\mathrm{T}}
\end{gather*}$$

## $\boldsymbol{A=U \Sigma V^{\mathrm{T}}}$

- Sec.7.1 (p.259) Singular Values and Singular Vectors

Every matrix (including rectangular one) has a singular value decomposition (SVD).
$A=U \Sigma V^{\mathrm{T}}$ has the singular vectors of $A$ in $U$ and $V$.
The following illustrates the 'reduced' SVD.

<figure data-latex-placement="H">
<embed src="SVD.eps" />
<figcaption><span class="math inline"><em>A</em> = <em>U</em><em>Σ</em><em>V</em><sup>T</sup></span></figcaption>
</figure>

You can find $V$ as an orthonormal basis of $\mathbb{R}^n$ (eigenvectors of $A^{\mathrm{T}}A$),
and $U$ as an orthonormal basis of $\mathbb{R}^m$ (eigenvectors of $AA^{\mathrm{T}}$).
Together they diagonalize $A$ into $\Sigma$.
This is also expressed as a combination of rank 1 matrices.

$$\begin{align*}
  A = U \Sigma V^{\mathrm{T}}=
  \begin{bmatrix}
    | & | & |\\
    \bm{u}_1 & \bm{u}_2 & \bm{u}_3\\
    | & | & |
  \end{bmatrix}
  \begin{bmatrix}
    \sigma_1 \\
           & \sigma_2 \\
           & &
  \end{bmatrix}
  \begin{bmatrix}
  - \bm{v}_1^{\mathrm{T}}-\\
  - \bm{v}_2^{\mathrm{T}}-
  \end{bmatrix}
  & =
  \sigma_1 \begin{bmatrix}
    |\\
    \bm{u}_1\\
    |
  \end{bmatrix}
  \begin{bmatrix}
    - \bm{v}_1^{\mathrm{T}}- 
  \end{bmatrix}
  +
  \sigma_2 \begin{bmatrix}
  |\\
  \bm{u}_2\\
  |
  \end{bmatrix}
  \begin{bmatrix}
  - \bm{v}_2^{\mathrm{T}}-
  \end{bmatrix} \\
& = \sigma_1 \bm{u}_1 \bm{v}_1^{\mathrm{T}}+ \sigma_2 \bm{u}_2 \bm{v}_2^{\mathrm{T}}
\end{align*}$$

Note that:

$$\begin{align*}
  U U^{\mathrm{T}}&= I_m \\
  V V^{\mathrm{T}}&= I_n
\end{align*}$$

See Pattern 4 (P4) for the graphic notation.

# Conclusion and Acknowledgements {#conclusion-and-acknowledgements .unnumbered}

I presented systematic visualizations of matrix/vector multiplication and
their application to the Five Matrix Factorizations. I hope you
enjoyed them and will use them
in your understanding of Linear Algebra.

Ashley Fernandes helped me with beautifying this paper in typesetting
and made it much more consistent and professional.

To conclude this paper, I'd like to thank Prof. Gilbert Strang for
publishing "Linear Algebra for Everyone\". It guides us
through a new vision to these beautiful landscapes in Linear Algebra.
Everyone can reach a fundamental understanding of its underlying ideas
in a practical manner that introduces us to contemporary and also
traditional data science and machine learning. An important part of the matrix world.

# References and Related Works {#references-and-related-works .unnumbered}

1.  Gilbert Strang(2020),*Linear Algebra for Everyone*, Wellesley Cambridge Press.,\
    <http://math.mit.edu/everyone>

2.  Gilbert Strang(2016), *Introduction to Linear Algebra*,Wellesley Cambridge Press, 5th ed.,\
    <http://math.mit.edu/linearalgebra>

3.  Kenji Hiranabe(2021), *Map of Eigenvalues*, Slidedeck,\
    <https://github.com/kenjihiranabe/The-Art-of-Linear-Algebra/blob/main/MapofEigenvalues.pdf>\

    <figure data-latex-placement="H">
    <embed src="MapofEigenvalues.eps" />
    <figcaption>Map of Eigenvalues</figcaption>
    </figure>

4.  Kenji Hiranabe(2020), *Matrix World*, Slidedeck,\
    <https://github.com/kenjihiranabe/The-Art-of-Linear-Algebra/blob/main/MatrixWorld.pdf>\

    <figure data-latex-placement="H">
    <embed src="MatrixWorld.eps" />
    <figcaption>Matrix World</figcaption>
    </figure>

5.  Gilbert Strang, artwork by Kenji Hiranabe, *The Four Subspaces and the solutions to $A\bm{x}=\bm{b}$*\

    <figure data-latex-placement="H">
    <embed src="TheFourSubspaces.eps" />
    <figcaption>The Four Subspaces and the solutions to <span class="math inline"><em>A</em><strong>x</strong> = <strong>b</strong></span></figcaption>
    </figure>

[^1]: "Linear Algebra for Everyone\":
    <http://math.mit.edu/everyone/> with Japanese translation started by Kindai Kagaku.

[^2]: twitter: \@hiranabe, k-hiranabe@esm.co.jp, <https://anagileway.com>

[^3]: Massachusetts Institute of Technology, <http://www-math.mit.edu/~gs/>
