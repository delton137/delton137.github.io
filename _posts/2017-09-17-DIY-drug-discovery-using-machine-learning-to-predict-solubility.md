---
id: 2000
title: DIY Drug Discovery - using molecular fingerprints and machine learning for solubility prediction
comments: true
author: delton137
layout: post
permalink: /2007/09/10/my-top-10-electronic-albums/
categories:
  - drug discovery
  - Python
  - machine learning

tags:
---

This is going to be the first in a series of posts on what I am calling "DIY Drug Discovery". Admittedly, though, this title is hyperbolic. Discovering drug drug requires bringing it through a series of trials, which is very hard, if not impossible for an individual to do themselves. What I'm really going to be discussing is drug screening.

# Background on chemical space and drug discovery

The set of all possible molecules, which is known as chemical space, is incredibly vast. The Chemical Abstracts Service (CAS) registry lists 49,037,297 known molecules (molecules that have actually be synthesized). The number of different molecules that have been synthesized, in both public and private settings, may reach towards 100,000,000. Yet this is only tiny fraction of the number of possible molecules.  Recent research has tried to enumerate the number of possible molecules containing Carbon, Nitrogen, Oxygen, Hydrogen, Oxygen, and halogens which may be of interest for drug discovery. So far, possible molecules up to a size of 17 atoms have been enumerated and a [large database](http://gdb.unibe.ch/downloads/) has been created. Enumerating possible molecules isn't as simple as enumerating possible molecular graphs. There are many physical constraints that the authors had to take into account. For instance:

* **bonding** many types of bonds are not possible -- covalent bonds must be between an electron donor and an electron acceptor. A Chlorine atom cannot bond to a flourine and a sodium cannot bond to a magnesium.

* **geometrical constraints** - Due to the nature of atomic orbitals, each atom prefers to bond in particular configuration. For instance, carbon prefers to bond tetrahedrally and when forming rings prefers to form hexagons. Pentagons and other shapes are not necessarily impossible, but they are generally high unstable. For instance, [https://en.wikipedia.org/wiki/Cubane](cubane), where carbon is forced to bond at 90 degrees, is highly unstable and explosive material. Carbon bonding in a triangle, or an isolated pentagon or decagon is impossible.

* **functional group stability** - Many arrangements may be structurally stable in isolation but are highly reactive, making them near impossible to contain in the real world.  For instance, if an oxygen or nitrogen atom is bonded to a non-aromatic C=C, this creates an Enol or enamine group which is highly reactive. The authors of the GBD database used 12 seperate filters to limit what types of functional groups could exist.

* **stereochemistry** - the basic idea of this constraint is that "two things cannot be in the same place at the same time". For instance, a molecule cannot loop back and intersect itself.

* **synthesizability** - the molecule most be synthesizable. For instance molecules with more than three carbon rings or allenes (C=C=C) are exceedingly difficult to synthesize.  

These basic physical constraints limit the chemical space significantly, especially if one is interested in . For instance the authors of GBD note "The vast majority of fused small ring systems are high strained and reactive. 96.7% of molecules with carbon are removed by this constraint. However, even after applying 29 filters, the GBD database still contains 10^11 molecules. This is a large number, but tractable in the sense that it could be stored on the very latest computer hardware. (storing the database in SMILES format would consume about 63 terabytes. The entire database is not available for public consumption, only a subset of 50 million compounds is downloadable). Keep in mind that this number was obtained after applying many constraints - the number of organic molecules of drug like size with normal atoms (CNOH + halogens) and up to 4 rings has been estimated to be around 10^60!

Apart from whether a molecule can physically exist and be synthesized, there are further constraints when it comes to making a drug:

* **solubility** the molecule must be soluble in the blood.

* **toxicity** the molecule cannot be toxic.

* **permeability & lipophilicity** can it get through any biological membranes it needs to, such cell wall or the blood brain barrier?

* **binding target affinity** will it actually bind to the target of interest?

Traditionally drug design has been done through a trial and error approach. A professor once described it to me as "trying to build an airplane by attaching the wings in at random orientations, and then seeing if it flies." Just as computer simulations are used to design highly aerodynamic airplanes, so that less actual physical assembly and testing needs to be done, physics based simulation holds the promise of being able to design and optimize drug molecules before they are actually syntheized.

It would be very helpful if machine learning could be used to screen molecules.



# Basic concepts of fingerprinting
*For more info an in easy to read format, see the [http://www.daylight.com/dayhtml/doc/theory/theory.finger.html](Daylight Information Systems page on fingerprinting).*

The first step in molecular machine learning is encoding the structure of the molecule in a form that is amenable to machine learning. This is where a lot of research is currently focused. A useful representation encodes features that are relevant and is efficient, so as to avoid the [curse of dimensionality](https://en.wikipedia.org/wiki/Curse_of_dimensionality). Fortunately, there is a way method of featurazation called fingerprinting which already has a long history of development in the world of drug discovery.

Fingerprinting was originally designed to solve the problem of molecular substructure search -- how do I find all the molecules in my database with a particular substructure? A related problem is molecular similarity - given a molecule, how do I find the molecules in my database that are most similar. Only later were fingerprints applied for machine learning, or what has traditionally called quantitative structure property relationships (QSPR).

Fingerprinting creates an efficient representation of the molecular graph. The basic process of fingerprinting is as follows: First the algorithm generates a set of patterns. For instance, enumeration of different paths is common:

0-bond paths:   |    1-bond paths: |
  C             |       OC         |
  O             |      C==C        |
  N             |       CN         |
2-bond paths:   |    3-bond paths: |
 OC=C           |       OC=CN      |
 C=CN           |                  |

<br>
Storing all this data would result in an enormous representation. The trick of fingerprinting is to “hash” each of these features, which essentially means they act as seeds to a random number generator called a hash function. The hash function generates a bit string. Typically the hash function is chosen so that 4 or 5 bits per pattern are non-zero in the bit string. Next, all of the bit strings are [https://en.wikipedia.org/wiki/OR_gate](OR)’ed together.

This process is very useful for substructure searching because every bit of the substructure’s fingerprint will be on (=1) in the molecule's fingerprint. Accidental collisions between patterns or substructures are possible, but if the bit density is low (known as a sparse representation) they are rare. Ideally, the on bit density of the bitstring should be tuned so as to reach a particular discriminatory power that is needed (ie. the chance that two structurally different molecules in my database have the same fingerprint is only 1%). There is a tradeoff between discriminatory power and the efficiency of the representation.

In practice, creating a bit density is done through folding. A very long, very sparse fingerprint is ‘folded’ down (with OR operations) to create a fingerprint with a desired length and good bit density. In case this is not obvious what this means, it can be literally thought of as folding the vector onto itself.

Now let's test some fingerprints. We use [rdkit.org](rdkit), an open source cheminformatics library. Our data consists of [https://en.wikipedia.org/wiki/Simplified_molecular-input_line-entry_system](SMILES) strings, which encode molecular graphs into a string of characters, and experimentally determined solubility values.


<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">from</span> <span class="nn">rdkit</span> <span class="k">import</span> <span class="n">Chem</span>
<span class="kn">from</span> <span class="nn">rdkit.Chem.EState</span> <span class="k">import</span> <span class="n">Fingerprinter</span>
<span class="kn">from</span> <span class="nn">rdkit.Chem</span> <span class="k">import</span> <span class="n">Descriptors</span>
<span class="kn">from</span> <span class="nn">rdkit.Chem.rdmolops</span> <span class="k">import</span> <span class="n">RDKFingerprint</span>
<span class="kn">import</span> <span class="nn">pandas</span> <span class="k">as</span> <span class="nn">pd</span>
<span class="kn">import</span> <span class="nn">numpy</span> <span class="k">as</span> <span class="nn">np</span>
<span class="kn">from</span> <span class="nn">sklearn.preprocessing</span> <span class="k">import</span> <span class="n">StandardScaler</span>
<span class="kn">from</span> <span class="nn">sklearn</span> <span class="k">import</span> <span class="n">cross_validation</span>
<span class="kn">from</span> <span class="nn">keras</span> <span class="k">import</span> <span class="n">regularizers</span>
<span class="kn">from</span> <span class="nn">keras.models</span> <span class="k">import</span> <span class="n">Sequential</span>
<span class="kn">from</span> <span class="nn">keras.layers</span> <span class="k">import</span> <span class="n">Dense</span><span class="p">,</span> <span class="n">Activation</span><span class="p">,</span> <span class="n">Dropout</span>
<span class="kn">from</span> <span class="nn">sklearn</span> <span class="k">import</span> <span class="n">cross_validation</span>
<span class="kn">from</span> <span class="nn">sklearn.kernel_ridge</span> <span class="k">import</span> <span class="n">KernelRidge</span>
<span class="kn">from</span> <span class="nn">sklearn.linear_model</span> <span class="k">import</span> <span class="n">Ridge</span><span class="p">,</span> <span class="n">LinearRegression</span>
<span class="kn">from</span> <span class="nn">sklearn.svm</span> <span class="k">import</span> <span class="n">SVR</span>
<span class="kn">from</span> <span class="nn">sklearn.neighbors</span> <span class="k">import</span> <span class="n">KNeighborsRegressor</span>
<span class="kn">from</span> <span class="nn">sklearn.gaussian_process</span> <span class="k">import</span> <span class="n">GaussianProcessRegressor</span>
<span class="kn">from</span> <span class="nn">sklearn.neural_network</span> <span class="k">import</span> <span class="n">MLPRegressor</span>
<span class="kn">from</span> <span class="nn">sklearn.ensemble</span> <span class="k">import</span> <span class="n">GradientBoostingRegressor</span><span class="p">,</span> <span class="n">RandomForestRegressor</span>
<span class="kn">from</span> <span class="nn">sklearn.model_selection</span> <span class="k">import</span> <span class="n">GridSearchCV</span>
<span class="kn">from</span> <span class="nn">rdkit.Avalon.pyAvalonTools</span> <span class="k">import</span> <span class="n">GetAvalonFP</span>

<span class="c1">#Read the data</span>
<span class="n">data</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">read_table</span><span class="p">(</span><span class="s1">&#39;../other_data_sets/solubility_data.txt&#39;</span><span class="p">,</span> <span class="n">sep</span><span class="o">=</span><span class="s1">&#39; &#39;</span><span class="p">,</span> <span class="n">skipfooter</span><span class="o">=</span><span class="mi">0</span><span class="p">)</span>

<span class="k">def</span> <span class="nf">estate_fingerprint_and_mw</span><span class="p">(</span><span class="n">mol</span><span class="p">):</span>
    <span class="k">return</span> <span class="n">np</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">FingerprintMol</span><span class="p">(</span><span class="n">mol</span><span class="p">)[</span><span class="mi">0</span><span class="p">],</span> <span class="n">Descriptors</span><span class="o">.</span><span class="n">MolWt</span><span class="p">(</span><span class="n">x</span><span class="p">))</span>

<span class="c1">#Add some new columns</span>
<span class="n">data</span><span class="p">[</span><span class="s1">&#39;Mol&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">data</span><span class="p">[</span><span class="s1">&#39;SMILES&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">apply</span><span class="p">(</span><span class="n">Chem</span><span class="o">.</span><span class="n">MolFromSmiles</span><span class="p">)</span>
<span class="n">num_mols</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">data</span><span class="p">)</span>

<span class="c1">#Create X and y</span>
<span class="c1">#Convert to Numpy arrays</span>
<span class="n">y</span> <span class="o">=</span> <span class="n">data</span><span class="p">[</span><span class="s1">&#39;Solubility&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">values</span>
</pre></div>

Next we make a bunch of different fingerprints. To do this, I have created a fingerprint object, which stores the name of the fingerprint and contains a method for applying the fingerprint and then converting the output into a NumPy array.

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">

<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">from</span> <span class="nn">rdkit.Chem.rdMolDescriptors</span> <span class="k">import</span>
<span class="kn">from</span> <span class="nn">rdkit.Chem.AtomPairs.Sheridan</span> <span class="k">import</span> <span class="n">GetBPFingerprint</span>
<span class="kn">from</span> <span class="nn">rdkit.Chem.EState.Fingerprinter</span> <span class="k">import</span> <span class="n">FingerprintMol</span>
<span class="kn">from</span> <span class="nn">rdkit.Avalon.pyAvalonTools</span> <span class="k">import</span> <span class="n">GetAvalonFP</span> <span class="c1">#GetAvalonCountFP  #int vector version</span>
<span class="kn">from</span> <span class="nn">rdkit.Chem.AllChem</span> <span class="k">import</span>  <span class="n">GetMorganFingerprintAsBitVect</span><span class="p">,</span> <span class="n">GetErGFingerprint</span>
<span class="kn">from</span> <span class="nn">rdkit.DataStructs.cDataStructs</span> <span class="k">import</span> <span class="n">ConvertToNumpyArray</span>
<span class="kn">import</span> <span class="nn">rdkit.DataStructs.cDataStructs</span>

<span class="k">def</span> <span class="nf">ExplicitBitVect_to_NumpyArray</span><span class="p">(</span><span class="n">bitvector</span><span class="p">):</span>
    <span class="n">bitstring</span> <span class="o">=</span> <span class="n">bitvector</span><span class="o">.</span><span class="n">ToBitString</span><span class="p">()</span>
    <span class="n">intmap</span> <span class="o">=</span> <span class="nb">map</span><span class="p">(</span><span class="nb">int</span><span class="p">,</span> <span class="n">bitstring</span><span class="p">)</span>
    <span class="k">return</span> <span class="n">np</span><span class="o">.</span><span class="n">array</span><span class="p">(</span><span class="nb">list</span><span class="p">(</span><span class="n">intmap</span><span class="p">))</span>


<span class="k">class</span> <span class="nc">fingerprint</span><span class="p">():</span>
    <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">fp_fun</span><span class="p">,</span> <span class="n">name</span><span class="p">):</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">fp_fun</span> <span class="o">=</span> <span class="n">fp_fun</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">name</span> <span class="o">=</span> <span class="n">name</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">x</span> <span class="o">=</span> <span class="p">[]</span>

    <span class="k">def</span> <span class="nf">apply_fp</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">mols</span><span class="p">):</span>
        <span class="k">for</span> <span class="n">mol</span> <span class="ow">in</span> <span class="n">mols</span><span class="p">:</span>
            <span class="n">fp</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">fp_fun</span><span class="p">(</span><span class="n">mol</span><span class="p">)</span>
            <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">fp</span><span class="p">,</span> <span class="nb">tuple</span><span class="p">):</span>
                <span class="n">fp</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">array</span><span class="p">(</span><span class="nb">list</span><span class="p">(</span><span class="n">fp</span><span class="p">[</span><span class="mi">0</span><span class="p">]))</span>
            <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">fp</span><span class="p">,</span> <span class="n">rdkit</span><span class="o">.</span><span class="n">DataStructs</span><span class="o">.</span><span class="n">cDataStructs</span><span class="o">.</span><span class="n">ExplicitBitVect</span><span class="p">):</span>
                <span class="n">fp</span> <span class="o">=</span> <span class="n">ExplicitBitVect_to_NumpyArray</span><span class="p">(</span><span class="n">fp</span><span class="p">)</span>
            <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">fp</span><span class="p">,</span><span class="n">rdkit</span><span class="o">.</span><span class="n">DataStructs</span><span class="o">.</span><span class="n">cDataStructs</span><span class="o">.</span><span class="n">IntSparseIntVect</span><span class="p">):</span>
                <span class="n">fp</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">array</span><span class="p">(</span><span class="nb">list</span><span class="p">(</span><span class="n">fp</span><span class="p">))</span>

            <span class="bp">self</span><span class="o">.</span><span class="n">x</span> <span class="o">+=</span> <span class="p">[</span><span class="n">fp</span><span class="p">]</span>

            <span class="k">if</span> <span class="p">(</span><span class="nb">str</span><span class="p">(</span><span class="nb">type</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">x</span><span class="p">[</span><span class="mi">0</span><span class="p">]))</span> <span class="o">!=</span> <span class="s2">&quot;&lt;class &#39;numpy.ndarray&#39;&gt;&quot;</span><span class="p">):</span>
                <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;WARNING: type for &quot;</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">name</span><span class="p">,</span> <span class="s2">&quot;is &quot;</span><span class="p">,</span> <span class="nb">type</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">x</span><span class="p">[</span><span class="mi">0</span><span class="p">]))</span>

<span class="k">def</span> <span class="nf">make_fingerprints</span><span class="p">(</span><span class="n">length</span> <span class="o">=</span> <span class="mi">512</span><span class="p">,</span> <span class="n">verbose</span><span class="o">=</span><span class="kc">False</span><span class="p">):</span>
    <span class="n">fp_list</span> <span class="o">=</span> <span class="p">[</span>
         <span class="c1">#fingerprint(lambda x : GetBPFingerprint(x, fpfn=AtomPair), </span>
         <span class="c1">#            &quot;Physiochemical properties (1996)&quot;), ##NOTE: takes a long time to compute</span>
         <span class="n">fingerprint</span><span class="p">(</span><span class="k">lambda</span> <span class="n">x</span> <span class="p">:</span> <span class="n">GetHashedAtomPairFingerprintAsBitVect</span><span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="n">nBits</span> <span class="o">=</span> <span class="n">length</span><span class="p">),</span>
                     <span class="s2">&qfuot;Atom pair (1985)&quot;</span><span class="p">),</span>
         <span class="n">fingerprint</span><span class="p">(</span><span class="k">lambda</span> <span class="n">x</span> <span class="p">:</span> <span class="n">GetHashedTopologicalTorsionFingerprintAsBitVect</span><span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="n">nBits</span> <span class="o">=</span> <span class="n">length</span><span class="p">),</span>
                     <span class="s2">&quot;Topological torsion (1987)&quot;</span><span class="p">),</span>
         <span class="n">fingerprint</span><span class="p">(</span><span class="k">lambda</span> <span class="n">x</span> <span class="p">:</span> <span class="n">GetMorganFingerprintAsBitVect</span><span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="n">nBits</span> <span class="o">=</span> <span class="n">length</span><span class="p">),</span>
                     <span class="s2">&quot;Morgan circular &quot;</span><span class="p">),</span>
         <span class="n">fingerprint</span><span class="p">(</span><span class="n">FingerprintMol</span><span class="p">,</span> <span class="s2">&quot;Estate (1995)&quot;</span><span class="p">),</span>
         <span class="n">fingerprint</span><span class="p">(</span><span class="k">lambda</span> <span class="n">x</span><span class="p">:</span> <span class="n">GetAvalonFP</span><span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="n">nBits</span><span class="o">=</span><span class="n">length</span><span class="p">),</span>
                    <span class="s2">&quot;Avalon bit based (2006)&quot;</span><span class="p">),</span>
         <span class="n">fingerprint</span><span class="p">(</span><span class="k">lambda</span> <span class="n">x</span><span class="p">:</span> <span class="n">np</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">GetAvalonFP</span><span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="n">nBits</span><span class="o">=</span><span class="n">length</span><span class="p">),</span> <span class="n">Descriptors</span><span class="o">.</span><span class="n">MolWt</span><span class="p">(</span><span class="n">x</span><span class="p">)),</span>
                    <span class="s2">&quot;Avalon+mol. weight&quot;</span><span class="p">),</span>
         <span class="n">fingerprint</span><span class="p">(</span><span class="k">lambda</span> <span class="n">x</span><span class="p">:</span> <span class="n">GetErGFingerprint</span><span class="p">(</span><span class="n">x</span><span class="p">),</span> <span class="s2">&quot;ErG fingerprint (2006)&quot;</span><span class="p">),</span>
         <span class="n">fingerprint</span><span class="p">(</span><span class="k">lambda</span> <span class="n">x</span> <span class="p">:</span> <span class="n">RDKFingerprint</span><span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="n">fpSize</span><span class="o">=</span><span class="n">length</span><span class="p">),</span>
                     <span class="s2">&quot;RDKit fingerprint&quot;</span><span class="p">)</span>
    <span class="p">]</span>

    <span class="k">for</span> <span class="n">fp</span> <span class="ow">in</span> <span class="n">fp_list</span><span class="p">:</span>
        <span class="k">if</span> <span class="p">(</span><span class="n">verbose</span><span class="p">):</span> <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;doing&quot;</span><span class="p">,</span> <span class="n">fp</span><span class="o">.</span><span class="n">name</span><span class="p">)</span>
        <span class="n">fp</span><span class="o">.</span><span class="n">apply_fp</span><span class="p">(</span><span class="nb">list</span><span class="p">(</span><span class="n">data</span><span class="p">[</span><span class="s1">&#39;Mol&#39;</span><span class="p">]))</span>

    <span class="k">return</span> <span class="n">fp_list</span>

<span class="n">fp_list</span> <span class="o">=</span> <span class="n">make_fingerprints</span><span class="p">()</span>

</pre></div>

</div>
</div>
</div>
</div>

The following code compares the fingerprints we have created, using 20 fold https://en.wikipedia.org/wiki/Cross-validation) and a ridge regression model.

<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="k">def</span> <span class="nf">test_model_cv</span><span class="p">(</span><span class="n">model</span><span class="p">,</span> <span class="n">x</span><span class="p">,</span> <span class="n">y</span><span class="p">,</span> <span class="n">cv</span><span class="o">=</span><span class="mi">20</span><span class="p">):</span>
    <span class="n">scores</span> <span class="o">=</span> <span class="n">cross_validation</span><span class="o">.</span><span class="n">cross_val_score</span><span class="p">(</span><span class="n">model</span><span class="p">,</span> <span class="n">x</span><span class="p">,</span> <span class="n">y</span><span class="p">,</span> <span class="n">cv</span><span class="o">=</span><span class="n">cv</span><span class="p">,</span> <span class="n">n_jobs</span><span class="o">=-</span><span class="mi">1</span><span class="p">,</span> <br><span class="n">scoring</span><span class="o">=</span><span class="s1">&#39;neg_mean_absolute_error&#39;</span><span class="p">)</span>

    <span class="n">scores</span> <span class="o">=</span> <span class="o">-</span><span class="mi">1</span><span class="o"></span><span class="n">scores</span>

    <span class="k">return</span> <span class="n">scores</span><span class="o">.</span><span class="n">mean</span><span class="p">()</span>


<span class="k">def</span> <span class="nf">test_fingerprints</span><span class="p">(</span><span class="n">fp_list</span><span class="p">,</span> <span class="n">model</span><span class="p">,</span> <span class="n">y</span><span class="p">,</span> <span class="n">verbose</span> <span class="o">=</span> <span class="kc">True</span><span class="p">):</span>

    <span class="n">fingerprint_scores</span> <span class="o">=</span> <span class="p">{}</span>

    <span class="k">for</span> <span class="n">fp</span> <span class="ow">in</span> <span class="n">fp_list</span><span class="p">:</span>
        <span class="k">if</span> <span class="n">verbose</span><span class="p">:</span> <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;doing &quot;</span><span class="p">,</span> <span class="n">fp</span><span class="o">.</span><span class="n">name</span><span class="p">)</span>
        <span class="n">fingerprint_scores</span><span class="p">[</span><span class="n">fp</span><span class="o">.</span><span class="n">name</span><span class="p">]</span> <span class="o">=</span> <span class="n">test_model_cv</span><span class="p">(</span><span class="n">model</span><span class="p">,</span> <span class="n">fp</span><span class="o">.</span><span class="n">x</span><span class="p">,</span> <span class="n">y</span><span class="p">)</span>

    <span class="n">sorted_names</span> <span class="o">=</span> <span class="nb">sorted</span><span class="p">(</span><span class="n">fingerprint_scores</span><span class="p">,</span> <span class="n">key</span><span class="o">=</span><span class="n">fingerprint_scores</span><span class="o">.</span><span class="fm">__getitem__</span><span class="p">,</span> <span class="n">reverse</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>

    <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;</span><span class="se">\\</span><span class="s2">begin</span><span class="si">{tabular}</span><span class="s2">{c c}&quot;</span><span class="p">)</span>
    <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;           name        &amp;  avg abs error in CV (kJ/cc) </span><span class="se">\\\\</span><span class="s2">&quot;</span><span class="p">)</span>
    <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;</span><span class="se">\\</span><span class="s2">hline&quot;</span><span class="p">)</span>
    <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="n">sorted_names</span><span class="p">)):</span>
        <span class="n">name</span> <span class="o">=</span> <span class="n">sorted_names</span><span class="p">[</span><span class="n">i</span><span class="p">]</span>
        <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;</span><span class="si">%30s</span><span class="s2"> &amp; </span><span class="si">%5.3f</span><span class="s2"> </span><span class="se">\\\\</span><span class="s2">&quot;</span> <span class="o">%</span> <span class="p">(</span><span class="n">name</span><span class="p">,</span> <span class="n">fingerprint_scores</span><span class="p">[</span><span class="n">name</span><span class="p">]))</span>
    <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;</span><span class="se">\\</span><span class="s2">end</span><span class="si">{tabular}</span><span class="s2">&quot;</span><span class="p">)</span>


<span class="n">test_fingerprints</span><span class="p">(</span><span class="n">fp_list</span><span class="p">,</span> <span class="n">Ridge</span><span class="p">(</span><span class="n">alpha</span><span class="o">=</span><span class="mf">1e-9</span><span class="p">),</span> <span class="n">y</span><span class="p">,</span> <span class="n">verbose</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>



</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">
<div class="prompt"></div>

<div class="output_subarea output_stream output_stdout output_text">
<pre>
doing  Atom pair (1985)
doing  Topological torsion (1987)
doing  Morgan circular
doing  Estate (1995)
doing  Avalon bit based (2006)
doing  Avalon+mol. weight
doing  ErG fingerprint (2006)
doing  RDKit fingerprint

\begin{tabular}{c c}
           name        &amp;  avg abs error in CV (kJ/cc) \\
\hline
                 Estate (1995) &amp; 0.699 \\
    Topological torsion (1987) &amp; 1.492 \\
        ErG fingerprint (2006) &amp; 1.697 \\
             RDKit fingerprint &amp; 2.869 \\
              Morgan circular  &amp; 2.928 \\
              Atom pair (1985) &amp; 3.043 \\
            Avalon+mol. weight &amp; 20.190 \\
       Avalon bit based (2006) &amp; 26.482 \\
\end{tabular}
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">

<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="k">def</span> <span class="nf">test_model_cv</span><span class="p">(</span><span class="n">model</span><span class="p">,</span> <span class="n">x</span><span class="p">,</span> <span class="n">y</span><span class="p">,</span> <span class="n">cv</span><span class="o">=</span><span class="mi">20</span><span class="p">):</span>
    <span class="n">scores</span> <span class="o">=</span> <span class="n">cross_validation</span><span class="o">.</span><span class="n">cross_val_score</span><span class="p">(</span><span class="n">model</span><span class="p">,</span> <span class="n">x</span><span class="p">,</span> <span class="n">y</span><span class="p">,</span> <span class="n">cv</span><span class="o">=</span><span class="n">cv</span><span class="p">,</span> <span class="n">n_jobs</span><span class="o">=-</span><span class="mi">1</span><span class="p">,</span> <span class="n">scoring</span><span class="o">=</span><span class="s1">&#39;neg_mean_absolute_error&#39;</span><span class="p">)</span>

    <span class="n">scores</span> <span class="o">=</span> <span class="o">-</span><span class="mi">1</span><span class="o"></span><span class="n">scores</span>

    <span class="k">return</span> <span class="n">scores</span><span class="o">.</span><span class="n">mean</span><span class="p">()</span>


<span class="k">def</span> <span class="nf">test_fingerprint_vs_size</span><span class="p">(</span><span class="n">model</span><span class="p">,</span> <span class="n">num_sizes_to_test</span> <span class="o">=</span> <span class="mi">20</span><span class="p">,</span> <span class="n">max_size</span><span class="o">=</span><span class="mi">2048</span><span class="p">,</span> <span class="n">cv</span> <span class="o">=</span> <span class="mi">20</span><span class="p">,</span> <span class="n">verbose</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span> <span class="n">makeplots</span><span class="o">=</span><span class="kc">False</span><span class="p">):</span>

    <span class="n">fp_list</span> <span class="o">=</span> <span class="n">make_fingerprints</span><span class="p">(</span><span class="n">length</span> <span class="o">=</span> <span class="mi">10</span><span class="p">)</span> <span class="c1">#test</span>
    <span class="n">num_fp</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">fp_list</span><span class="p">)</span>

    <span class="n">sizes</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">linspace</span><span class="p">(</span><span class="mi">100</span><span class="p">,</span><span class="n">max_size</span><span class="p">,</span><span class="n">num_sizes_to_test</span><span class="p">)</span>

    <span class="n">scores_vs_size</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">zeros</span><span class="p">([</span><span class="n">num_fp</span><span class="p">,</span> <span class="n">num_sizes_to_test</span><span class="p">])</span>

    <span class="n">num_fp</span> <span class="o">=</span> <span class="mi">0</span>
    <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="n">num_sizes_to_test</span><span class="p">):</span>
        <span class="k">if</span> <span class="n">verbose</span><span class="p">:</span> <span class="nb">print</span><span class="p">(</span><span class="n">i</span><span class="p">,</span> <span class="s2">&quot;,&quot;</span><span class="p">,</span> <span class="n">end</span><span class="o">=</span><span class="s1">&#39;&#39;</span><span class="p">)</span>
        <span class="n">length</span> <span class="o">=</span> <span class="n">sizes</span><span class="p">[</span><span class="n">i</span><span class="p">]</span>
        <span class="n">fp_list</span> <span class="o">=</span> <span class="n">make_fingerprints</span><span class="p">(</span><span class="n">length</span> <span class="o">=</span> <span class="nb">int</span><span class="p">(</span><span class="n">length</span><span class="p">))</span>
        <span class="n">num_fp</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">fp_list</span><span class="p">)</span>
        <span class="k">for</span> <span class="n">j</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="n">num_fp</span><span class="p">):</span>
            <span class="n">scores_vs_size</span><span class="p">[</span><span class="n">j</span><span class="p">,</span><span class="n">i</span><span class="p">]</span> <span class="o">=</span> <span class="n">test_model_cv</span><span class="p">(</span><span class="n">model</span><span class="p">,</span> <span class="n">fp_list</span><span class="p">[</span><span class="n">j</span><span class="p">]</span><span class="o">.</span><span class="n">x</span><span class="p">,</span> <span class="n">y</span><span class="p">)</span>

    <span class="k">if</span> <span class="p">(</span><span class="n">makeplots</span><span class="p">):</span>
        <span class="kn">import</span> <span class="nn">matplotlib.pyplot</span> <span class="k">as</span> <span class="nn">plt</span>
        <span class="n">plt</span><span class="o">.</span><span class="n">clf</span><span class="p">()</span>
        <span class="n">fig</span> <span class="o">=</span> <span class="n">plt</span><span class="o">.</span><span class="n">figure</span><span class="p">(</span><span class="n">figsize</span><span class="o">=</span><span class="p">(</span><span class="mi">10</span><span class="p">,</span><span class="mi">10</span><span class="p">))</span>
        <span class="n">fp_names</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="n">num_fp</span><span class="p">):</span>
            <span class="n">plt</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">sizes</span><span class="p">,</span> <span class="n">scores_vs_size</span><span class="p">[</span><span class="n">i</span><span class="p">,:],</span><span class="s1">&#39;-&#39;</span><span class="p">)</span>
            <span class="n">fp_names</span> <span class="o">+=</span> <span class="p">[</span><span class="n">fp_list</span><span class="p">[</span><span class="n">i</span><span class="p">]</span><span class="o">.</span><span class="n">name</span><span class="p">]</span>
        <span class="n">plt</span><span class="o">.</span><span class="n">title</span><span class="p">(</span><span class="s1">&#39;Ridge regression, average CV score vs fingerprint length&#39;</span><span class="p">,</span><span class="n">fontsize</span><span class="o">=</span><span class="mi">25</span><span class="p">)</span>
        <span class="n">plt</span><span class="o">.</span><span class="n">ylabel</span><span class="p">(</span><span class="s1">&#39;average mean absolute error in CV &#39;</span><span class="p">,</span><span class="n">fontsize</span><span class="o">=</span><span class="mi">20</span><span class="p">)</span>
        <span class="n">plt</span><span class="o">.</span><span class="n">xlabel</span><span class="p">(</span><span class="s1">&#39;fingerprint length&#39;</span><span class="p">,</span> <span class="n">fontsize</span><span class="o">=</span><span class="mi">20</span><span class="p">)</span>
        <span class="n">plt</span><span class="o">.</span><span class="n">legend</span><span class="p">(</span><span class="n">fp_names</span><span class="p">,</span><span class="n">fontsize</span><span class="o">=</span><span class="mi">15</span><span class="p">)</span>
        <span class="n">plt</span><span class="o">.</span><span class="n">ylim</span><span class="p">([</span><span class="o">.</span><span class="mi">2</span><span class="p">,</span><span class="mi">4</span><span class="p">])</span>
        <span class="n">plt</span><span class="o">.</span><span class="n">show</span><span class="p">()</span>

    <span class="k">return</span> <span class="n">scores_vs_size</span>


<span class="n">scores_vs_size</span> <span class="o">=</span> <span class="n">test_fingerprint_vs_size</span><span class="p">(</span><span class="n">Ridge</span><span class="p">(</span><span class="n">alpha</span><span class="o">=</span><span class="mf">1e-9</span><span class="p">),</span> <span class="n">verbose</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span> <span class="n">makeplots</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
</pre></div>


<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
2Ga1WklKSnJ5/ZqWplbkSym9+rFeuHAhnTp1cjEFAbjhhhtYvny5V3vguqix1w5pHi4f1gBZKY3z
xu5PkJigewUJs6s9Hacva1c7a7vNxoGd200zkACxREWR0bwlhXt+IyrKQv/RHakorearZcE3D6wP
W74qwFplo0v/lpFuikmIMQVrk5BQUFBAv379sNlsvP3228ycOZNPPvmEK6+8spZN8cSJE8nKymLp
0qXcfPPN/O1vf+O1115zpG/cuJGrrrqK5s2bs2zZMh5++GH+85//uGgRPXHzzTfz5ptv8thjj7Fs
2TKaNm3KFVdcwYYNGxx5nnnmGWbMmMHdd9/N4sWLAXjwwQfrPL6HHnqICRMmMGDAAN59913mzp1L
QkKCQ7DNz8+nT58+vPrqq7z77rtcc801jBw5kuXLl/vdh4MHD+bOO+8kNjbWYZowa9asgPtkzJgx
9OrVi/fff5/Ro0ezcuVK7rrrLm655RZWrFjBa6+9Ro8ePXzatt5///3MmDGD8ePH895779G9e3eG
DRtW63h27NjBQw89xNSpU1mwYAF79uzhxhtv9HmcJSUlfP/991xwwQV+943O8ePHgdpu6mJjY9m+
fbtjrI0ePZrd+bt48V9zKCkp4bfffmPSpEl07tyZiy++GLV40XXhYGFhIZ9++qnHPr3ggguorKzk
q6++CrjN4NndXnh8WDfOqIs6dQnWmfGZHK066ngwCQrHDoC1POwa64TkFBJT0yja5+oZ5Mie36ip
qjIjLtaDrJatObLndwCatm5Cl8ta8euX+9m3LUTROv3Ebpds+mwPeW1Tadq6SUTbYhJ6Iv9+xAQ+
ngIHforMvnPPgYFPB73aZ555hri4OFasWOF4pXvaaadxySWX8P777zNo0CBH3m7dujFnzhwArrji
Cvbv38+0adO49dZbAXjsscdo3749y5Ytc2gxU1JSuPnmm9m4cSNdu3attf8ffviBZcuW8fbbbzN8
+HBH3R07dmT69Om8++67VFdX89xzz3H33Xfz8MMPO/L079+fvXt9REQ7fJi///3vTJkyhSeffNKx
/YYbbnD8vummmxy/7XY7l1xyCfn5+bzyyisux+6Lpk2b0qpVK4QQtUwOAumTUaNG8eijjzr+T5s2
jR49ejB58mTHtuuuu85rOw4ePMjcuXN5/PHHuf/++wHVT7/99htTp051OZ6ioiLWr19P69bK3vH4
8eOMHDmS/Px82rRp47H+77//HiklZ599tl/9YqRdO+Ue7dtvv+Wyyy4DVH9/99132Gw2SktLycjI
oOv/deEAACAASURBVGePnrz+8kLG3vUnpjz4VwDOPvtsPvnkE+XizoPGeunSpVitVkaMGFErLScn
h5ycHDZs2MAVV1wRcLs9eQVp0iT0N9wj5coUpLF6BdH7oC5f1iVVJWQlZAVnpxHwCKKTnte8lss9
PTCMGXExcDJbtmbz2jVUVZQTl5hEz2tOY9cPh/ls/hZGPNyT6NjILBj87acjlB45Tu9B4XHnaBJZ
TI21SUjYsGGDw/xA5+KLLyY3N5e1a9e65HUXNAcPHkx+fj6HDh1y1HXDDTe4mAYMGzYMIUStuoz7
j4qKYvDgwY5tUVFRDBkyxFFm165dFBYWcu2117qUdf/vztq1a6muruZPf/qT1zyFhYWMHz+eVq1a
ERsbS0xMDG+88YbD3KKhBNIn7h4szj33XNavX8+kSZNYu3YtVqvV575+/PFHqqqqGDp0qMv24cOH
s2nTJhdNd/v27R1CNcCZZ54J4PNBRTe5ycoKXFDq3r073bt3Z+LEifzwww8cOnSISZMmkZ+fDzjN
Sb7/fiPj7/kzI4aNZNWqVSxfvpz4+HiuuuoqKioqPPqxXrhwId26deOMM87wuO+srCxH2wPFXbAO
m431sSqEgIykxqmxTk5W9u91CdZBdbnn8GEd/oWCGc1bUOwmWO/ftoXE1DSaZJvu2AIlS1vAWLhX
aa1jYqPoN6oDRw9X8s2HuyPWrh9X7yE5PY7Tzw3Sw6BJo8bUWDcGQqAxjjQFBQVceOGFtbbn5ORQ
VOR6U2zatKnH/wUFBWRnZ3Pw4EFycnJc8sTHx9OkSZNadRn3n56eXstuNScnh+Ji9VpQF4qys7Nd
8rj/d6ewsBCAvLw8r3luvPFGfv75Zx566CE6duxISkoKs2fPrmXjXR+klAH1iXu+q6++mpdeeom5
c+fy3HPPkZqays0338zTTz/tcWGjvoDQvR79f3FxsUPTqNst6+jCom6y4Qk9LS4ucC2qEIL58+cz
dOhQh5a+S5cujB8/nldeeYXU1FRAme6cdeY5zJkzl9h4Ne1deOGFtGjRgnnz5nHjDYNcTEEKCgr4
4osvePbZZ73uOy4uzudx+cJ98WI4bazTE2OJjmqcOpXo6GgSExPDG9a8aCdExUJq+G1fM/KaU3ms
lMpjpSSkqGtIBYbpaAYPqQe6YH1kz280a68WIrfomEGnC/PY+N89tOuWQ3arlLC26cjeMvZtLaH3
oLZYGul1ZxJczLNsEhLy8vIcGmcjBw8eJCMjw2Wbez79f15eHkIIcnJyauU5fvy44zW/t/0XFxfX
0sYePHiQ9HSl9crNzQWUaYcR9//uZGaqEMO6wOlOaWkpK1euZPr06dxxxx3069eP7t27+/RXHQiB
9omnG/Rtt93Gxo0bOXDgANOnT+df//oXzzzzjMf96Q8Q7vs7ePAggKM/64ve3pKSknqV79ixIz/9
9BM7duxg69atbNy4kfLycnr27Ok49q3btnJWp3Ncoi5mZ2fTvHlzdu7cWcsUZPHixUgpHWZEnigp
KfE6/upCt7GOtighP2w21mVVjda+WseXL+v0OC2seTAF68KdkN4GLOE3E8horoR5fQFj5bFSigv2
mQsX60mTrGxi4hM4suc3l+0XDG5HQnIMq+dvdkRgDRebPttDdIyFM/s0C+t+TSKHKVibhIRevXrx
0UcfUVFR4dj25ZdfcuDAAfr06eOS130B3LJly2jdurVDc92rVy+WLl3q4tt2yZIlSClr1aXTs2dP
bDabS902m42lS5c6ypx++ulkZmby7rvvupR97733fB5bnz59iI2N5fXXX/eYri9gNGpgi4uL+eij
j3zW64nY2FisVit2u+vNoD594omcnBzGjx9Pr169+PXXXz3m6dKlC3FxcbW8gCxevJjOnTs32Da4
QwclROze3bBXtW3btqV9+/YcOnSIpUuXOmz0AVq1bMlPv2zCYoi6ePDgQfbu3avZfrsagyxcuJCL
LrqIFi1aeNyX1Wpl3759tG/fvl5tNZqC2O12ampqwuZuLzOpcdpX6/iKvhgSU5AIeATRSXe43NsD
wIEdylSsmSlY1wthsZDVohWFboJ1fFIMF49sz5E9Zfzw6Z6wtafyWDXb1h+kQ+884pNC/0bKpHFg
moKYhITJkyfz6quvMnDgQCZNmkRxcTFTpkyhW7duXHPNNS55v/vuO+68806uueYaVq1axYIFC3j5
5Zcd6Y888gg9evTghhtu4M9//jO7d+9mypQpXHfddR4XLoKyIx48eDBjx46lqKiI1q1b8+KLL5Kf
n8+bb74JKKH13nvv5ZFHHiE9PZ1evXrxzjvvsH37dsC7u7fs7GymTJnCtGnTqKio4Morr6SiooL3
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
9OnTh+7du3P0qPPo9Oeff56LL76YpUuXsn37dv73f/+X1NRUHn74YaZOncpf/vIXnn/+edavXw9A
REREmz/X1atX06dPH2JjT53DW1xczP79+7ntttvsx/bs2UP//v0d1gUEBNCrVy/27NljXwO0sur0
69ePsrIyiouLMRgMbNiwgYEDBzJ37lxee+01qquryczM5NVXX6Vfv34O544aNYo1a1bzyANzWgnr
k8NhPP8rzpYIEqR3/kmFKzrWOUXVBOh19Ig59Zhsn6A0FwOlHKmq07oSl5EakUpKeArZhdlc3/d6
rcvxSezJIPmHCI2K1rgahTehhLWiQ5SWljrtuh08eJC0tDT74xEjRvD666/bH//rX/8CsPtzbVgs
FiwWi/1xS4FuIzk52S7iBg0aZBe/bQlrf39/li9fbr/erl27+Pjjj+3C+t1336W0tJTNmzeTlGT9
yLVXr14MHz7c4TqPPPIIo0aNstcPkJSUxCWXXMKOHTscRPj999/Pn/70J/vjvLw8AAYMGMBbb70F
wMSJEykqKuL//u//uPvuu+1Whrq6Ol544QWuuOIK+/ltCeu0tDQWL15sv966dev497//zcMPP4zB
YLD/OZyOjWTLli0Or6Et/vKXvxAWFubQzS8vL3d4A2EjOjqa8vJy+xqg1bro6Gj78waDgWPHjrF1
61Z2797N22+/jZ+fH48//jiTJk1i7969Draa8847j1dffRWj0YhO79i5PTkcxvNxZaZGE0KINrON
XWIFKaohPS4UP7360JGyXAz+RnZWVLoscUVrhBCMTR7LZ/s+w9ho9esrPItdWB8+ROqgwRpXo/Am
lLDuBHS0Y6wlkZGRrFq1qtXx7t27OzyeOnWq0/NbetYuv/xyvv76a/vj33777bSEXntcdNFFDiK9
f//+FBUV2f8B3rRpExdccIFdVANceOGFdOvWzf64traW9evX8+qrrzp06ceMGYO/v38rUdrWa54+
3XHgw1VXXcU//vEPCgoK6NGjB2D9uUyePPm0XlvLrn///v3ZvHnzaZ3bkmPHjrW7OfLNN99k6dKl
fPbZZ+12tjuKlJITJ07w2Wef2TvUAwYMoE+fPnz44YcOnfK4uDjMZjOlZSWk6AwO19FyOIzRbCRA
H+A0EQRcI6z3F9UwoHvkWV2jy1B6AENEBJRCSUkJiYmJWlfkEjKTMvlg9wdsOraJzORMrcvxOUIi
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
RERERDxAwVpERERExAMUrEVEREREPEDBWkRERETEAxSsRUREREQ8QMFaRERERMQDFKxFRERERDxA
wVpERERExAMUrEVEREREPEDBWkRERETEAxSsRUREREQ8QMFaRERERMQDFKxFRERERDxAwVpERERE
xAMUrEVEREREPEDBWkRERETEA3p0sDbGLDDGHDHGHDPGfLWd++cYY6qMMfvdl297o04RERER6foC
vF2Atxhj/IHfA7cCp4Bdxpg3rLWHztt1s7V2UacXKCIiIiI+pSf3WE8Fjllrc6y1TcBy4C4v1yQi
IiIiPqonB+skIK/N7VPubeebYYw5YIx52xgzpr0DGWM+ZYzZbYzZXVJScj1qFREREZEuricH647Y
Cwy01o4Hfgu81t5O1tq/WGvTrLVpffv27dQCRURERKRr6MnBOh8Y0OZ2f/e2s6y11dbaM+7rbwGB
xpjYzitRRERERHxFTw7Wu4DhxphkY0wQsBR4o+0Oxph4Y4xxX5+Kq73KOr1SEREREenyeuysINba
FmPMZ4HVgD/wnLU2wxjzhPv+PwH3AZ8xxrQA9cBSa631WtEiIiIi0mUZ5UTPSktLs7t37/Z2GSIi
IiKXZYzZY61N83Yd3UVPHgoiIiIiIuIxCtYiIiIiIh6gYC0iIiIi4gEK1iIiIiIiHqBgLSIiIiLi
AQrWIiIiIiIeoGAtIiIiIuIBCtYiIiIiIh6gYC0iIiIi4gEK1iIiIiIiHqBgLSIiIiLiAQrWIiIi
IiIeoGAtIiIiIuIBCtYiIiIiIh6gYC0iIiIi4gEK1iIiIiIiHqBgLSIiIiLiAQrWIiIiIiIeoGAt
IiIiIuIBCtYiIiIiIh6gYC0iIiIi4gEK1iIiIiIiHqBgLSIiIiLiAQrWIiIiIiIeoGAtIiIiIuIB
CtYiIiIiIh6gYC0iIiIi4gEK1iIiIiIiHqBgLSIiIiLiAQrWIiIiIiIeoGAtIiIiIuIBCtYiIiIi
Ih6gYC0iIiIi4gEK1iIiIiIiHqBgLSIiIiLiAQrWIiIiIiIeoGAtIiIiIuIBxlrr7Rq6FWNMCXDC
23V4USxQ6u0iugC1g9oA1AagNgC1AagNoOu2wSBrbV9vF9FdKFiLRxljdltr07xdh7epHdQGoDYA
tQGoDUBtAGqDnkJDQUREREREPEDBWkRERETEAxSsxdP+4u0Cugi1g9oA1AagNgC1AagNQG3QI2iM
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
YII=
"
>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>We see that the Estate fingerprint performs best. This is not suprising as Estate encodes information about the effective charge on each atom. For other applications I have tried, the avalon or atom pair fingerprints often perform best. Estate has a fixed length of 80. We create the array X using the Estate fingerprint to feed into machine learning models:</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">

<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="k">def</span> <span class="nf">estate_fingerprint</span><span class="p">(</span><span class="n">mol</span><span class="p">):</span>
    <span class="k">return</span> <span class="n">FingerprintMol</span><span class="p">(</span><span class="n">mol</span><span class="p">)[</span><span class="mi">0</span><span class="p">]</span>

<span class="c1">#Scale X to unit variance and zero mean</span>
<span class="n">data</span><span class="p">[</span><span class="s1">&#39;Fingerprint&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">data</span><span class="p">[</span><span class="s1">&#39;Mol&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">apply</span><span class="p">(</span><span class="n">estate_fingerprint</span><span class="p">)</span>

<span class="n">X</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">array</span><span class="p">(</span><span class="nb">list</span><span class="p">(</span><span class="n">data</span><span class="p">[</span><span class="s1">&#39;Fingerprint&#39;</span><span class="p">]))</span>

<span class="n">st</span> <span class="o">=</span> <span class="n">StandardScaler</span><span class="p">()</span>
<span class="n">X</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">array</span><span class="p">(</span><span class="nb">list</span><span class="p">(</span><span class="n">data</span><span class="p">[</span><span class="s1">&#39;Fingerprint&#39;</span><span class="p">]))</span>
<span class="n">X</span> <span class="o">=</span> <span class="n">st</span><span class="o">.</span><span class="n">fit_transform</span><span class="p">(</span><span class="n">X</span><span class="p">)</span>

</pre></div>
</div>
</div>
</div>
</div>

Next we do grid searches to tune the hyperparameters of the KernelRidge, Ridge, GaussianProcessRegressor, and RandomForestRegressor models in sci-kit-learn:

<div class="cell border-box-sizing code_cell rendered">
<div class="input">

<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">KRmodel</span> <span class="o">=</span> <span class="n">GridSearchCV</span><span class="p">(</span><span class="n">KernelRidge</span><span class="p">(),</span> <span class="n">cv</span><span class="o">=</span><span class="mi">10</span><span class="p">,</span>
              <span class="n">param_grid</span><span class="o">=</span><span class="p">{</span><span class="s2">&quot;alpha&quot;</span><span class="p">:</span> <span class="n">np</span><span class="o">.</span><span class="n">logspace</span><span class="p">(</span><span class="o">-</span><span class="mi">10</span><span class="p">,</span> <span class="o">-</span><span class="mi">5</span><span class="p">,</span> <span class="mi">10</span><span class="p">),</span>
             <span class="s2">&quot;gamma&quot;</span><span class="p">:</span> <span class="n">np</span><span class="o">.</span><span class="n">logspace</span><span class="p">(</span><span class="o">-</span><span class="mi">12</span><span class="p">,</span> <span class="o">-</span><span class="mi">9</span><span class="p">,</span> <span class="mi">10</span><span class="p">),</span> <span class="s2">&quot;kernel&quot;</span> <span class="p">:</span> <span class="p">[</span><span class="s1">&#39;laplacian&#39;</span><span class="p">,</span> <span class="s1">&#39;rbf&#39;</span><span class="p">]},</span> <span class="n">scoring</span><span class="o">=</span><span class="s1">&#39;neg_mean_absolute_error&#39;</span><span class="p">,</span> <span class="n">n_jobs</span><span class="o">=-</span><span class="mi">1</span><span class="p">)</span>

<span class="n">KRmodel</span> <span class="o">=</span> <span class="n">KRmodel</span><span class="o">.</span><span class="n">fit</span><span class="p">(</span><span class="n">X</span><span class="p">,</span> <span class="n">y</span><span class="p">)</span>
<span class="n">Best_KernelRidge</span> <span class="o">=</span> <span class="n">KRmodel</span><span class="o">.</span><span class="n">best_estimator_</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Best Kernel Ridge model&quot;</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">KRmodel</span><span class="o">.</span><span class="n">best_params_</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="o">-</span><span class="mi">1</span><span class="o">*</span><span class="n">KRmodel</span><span class="o">.</span><span class="n">best_score_</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">
<div class="prompt"></div>

<div class="output_subarea output_stream output_stdout output_text">
<pre>Best Kernel Ridge model
{&#39;alpha&#39;: 3.5938136638046258e-10, &#39;gamma&#39;: 1e-10, &#39;kernel&#39;: &#39;laplacian&#39;}
0.710770578217
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">

<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">Rmodel</span> <span class="o">=</span> <span class="n">GridSearchCV</span><span class="p">(</span><span class="n">Ridge</span><span class="p">(),</span> <span class="n">cv</span><span class="o">=</span><span class="mi">20</span><span class="p">,</span>
              <span class="n">param_grid</span><span class="o">=</span><span class="p">{</span><span class="s2">&quot;alpha&quot;</span><span class="p">:</span> <span class="n">np</span><span class="o">.</span><span class="n">logspace</span><span class="p">(</span><span class="o">-</span><span class="mi">10</span><span class="p">,</span> <span class="o">-</span><span class="mi">5</span><span class="p">,</span> <span class="mi">30</span><span class="p">),},</span> <span class="n">scoring</span><span class="o">=</span><span class="s1">&#39;neg_mean_absolute_error&#39;</span><span class="p">,</span> <span class="n">n_jobs</span><span class="o">=-</span><span class="mi">1</span><span class="p">)</span>

<span class="n">Rmodel</span> <span class="o">=</span> <span class="n">Rmodel</span><span class="o">.</span><span class="n">fit</span><span class="p">(</span><span class="n">X</span><span class="p">,</span> <span class="n">y</span><span class="p">)</span>
<span class="n">Best_Ridge</span> <span class="o">=</span> <span class="n">Rmodel</span><span class="o">.</span><span class="n">best_estimator_</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Best Ridge model&quot;</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">Rmodel</span><span class="o">.</span><span class="n">best_params_</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="o">-</span><span class="mi">1</span><span class="o">*</span><span class="n">Rmodel</span><span class="o">.</span><span class="n">best_score_</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">
<div class="prompt"></div>

<div class="output_subarea output_stream output_stdout output_text">
<pre>Best Ridge model
{&#39;alpha&#39;: 1e-10}
0.699188630722
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">

<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">GPmodel</span> <span class="o">=</span> <span class="n">GridSearchCV</span><span class="p">(</span><span class="n">GaussianProcessRegressor</span><span class="p">(</span><span class="n">normalize_y</span><span class="o">=</span><span class="kc">True</span><span class="p">),</span> <span class="n">cv</span><span class="o">=</span><span class="mi">20</span><span class="p">,</span>
              <span class="n">param_grid</span><span class="o">=</span><span class="p">{</span><span class="s2">&quot;alpha&quot;</span><span class="p">:</span> <span class="n">np</span><span class="o">.</span><span class="n">logspace</span><span class="p">(</span><span class="o">-</span><span class="mi">15</span><span class="p">,</span> <span class="o">-</span><span class="mi">10</span><span class="p">,</span> <span class="mi">30</span><span class="p">),},</span> <span class="n">scoring</span><span class="o">=</span><span class="s1">&#39;neg_mean_absolute_error&#39;</span><span class="p">,</span> <span class="n">n_jobs</span><span class="o">=-</span><span class="mi">1</span><span class="p">)</span>
<span class="n">GPmodel</span> <span class="o">=</span> <span class="n">GPmodel</span><span class="o">.</span><span class="n">fit</span><span class="p">(</span><span class="n">X</span><span class="p">,</span> <span class="n">y</span><span class="p">)</span>
<span class="n">Best_GaussianProcessRegressor</span> <span class="o">=</span> <span class="n">GPmodel</span><span class="o">.</span><span class="n">best_estimator_</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Best Gaussian Process model&quot;</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">GPmodel</span><span class="o">.</span><span class="n">best_params_</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="o">-</span><span class="mi">1</span><span class="o">*</span><span class="n">GPmodel</span><span class="o">.</span><span class="n">best_score_</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">
<div class="prompt"></div>

<div class="output_subarea output_stream output_stdout output_text">
<pre>Best Gaussian Process model
{&#39;alpha&#39;: 2.2122162910704501e-15}
0.965220889797
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">

<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">RFmodel</span> <span class="o">=</span> <span class="n">GridSearchCV</span><span class="p">(</span><span class="n">RandomForestRegressor</span><span class="p">(),</span> <span class="n">cv</span><span class="o">=</span><span class="mi">20</span><span class="p">,</span>
              <span class="n">param_grid</span><span class="o">=</span><span class="p">{</span><span class="s2">&quot;n_estimators&quot;</span><span class="p">:</span> <span class="n">np</span><span class="o">.</span><span class="n">linspace</span><span class="p">(</span><span class="mi">50</span><span class="p">,</span> <span class="mi">150</span><span class="p">,</span> <span class="mi">25</span><span class="p">)</span><span class="o">.</span><span class="n">astype</span><span class="p">(</span><span class="s1">&#39;int&#39;</span><span class="p">)},</span> <span class="n">scoring</span><span class="o">=</span><span class="s1">&#39;neg_mean_absolute_error&#39;</span><span class="p">,</span> <span class="n">n_jobs</span><span class="o">=-</span><span class="mi">1</span><span class="p">)</span>

<span class="n">RFmodel</span> <span class="o">=</span> <span class="n">RFmodel</span><span class="o">.</span><span class="n">fit</span><span class="p">(</span><span class="n">X</span><span class="p">,</span> <span class="n">y</span><span class="p">)</span>
<span class="n">Best_RandomForestRegressor</span> <span class="o">=</span> <span class="n">RFmodel</span><span class="o">.</span><span class="n">best_estimator_</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Best Random Forest model&quot;</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">RFmodel</span><span class="o">.</span><span class="n">best_params_</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="o">-</span><span class="mi">1</span><span class="o">*</span><span class="n">RFmodel</span><span class="o">.</span><span class="n">best_score_</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">
<div class="prompt"></div>

<div class="output_subarea output_stream output_stdout output_text">
<pre>Best Random Forest model
{&#39;n_estimators&#39;: 91}
0.64131656385
</pre>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>



# Testing out different machine learning models

asdf
