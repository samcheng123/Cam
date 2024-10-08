---
layout: archive
title: "CV"
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---

{% include base_path %}

Education
======
* PhD in Applied Mathematics, DAMTP, University of Cambridge, 2021-2025
* MMath and BA, University of Cambridge, 2017-2021
* (Incomplete) BEng(CompSc), University of Hong Kong, 2015-2017
<!-- * B.S. in GitHub, GitHub University, 2012 -->

Work experience
======
* 2024 Nov-2025 Mar: GSK.ai AI/ML
  * Latent geometry of neural networks.
  * Supervisors: Dr. Emma Slade, Dr. Alexandra Pettet

* 2023 Jul-Aug: Research Exchange
  * University of California, Los Angeles (UCLA)
  * New numerical methods for sampling. See [this paper](https://arxiv.org/abs/2308.14945).
  * Supervisors: Prof. Stanley J. Osher, Prof. Wuchen Li

* 2022 Jan-Jun: External Research Assistant
  * Schlumberger
  * Numerical method to separate mixed signals with greedy fitting.
  * Supervisor: Dr. Can Evren Yarman

* 2021 Aug-Oct: Summer Intern
  * Faraday Predictive
  * Signal spectral abnormality detection in the low-data regime using clustering techniques.
  * Supervisors: Geoff Walker, Andrew Bates

* 2021 Jul-Aug: Summer Intern
  * Applied Cryptosystems Department, ASTRI
  * Testing federated machine learning frameworks for secure distributed learning.
  * Supervisor: Dr. Kam Hong Shum

* 2020 Jul-Sep: Summer Research Assistant
  * DAMTP, University of Cambridge
  * Researching methods to predict glioblastoma subtypes using MRI and histology.
  * Supervisor: Dr. Chao Li
  
Skills
======
* Programming
  * Main: Python, PyTorch
  * Probably OK: JAX, MATLAB
  * Very rusty: C, C++, Java, Haskell
* Languages: English, Mandarin Chinese, Cantonese

Publications
======
  <ul>{% for post in site.publications reversed %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>
  
Talks
======
  <ul>{% for post in site.talks reversed %}
    {% include archive-single-talk-cv.html  %}
  {% endfor %}</ul>
  
<!-- Teaching
======
  <ul>{% for post in site.teaching reversed %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul> -->
  
Others
======
* Third generation scholar of the [Masason Foundation](https://masason-foundation.org/en/)
* Reviewer for Inverse Problems and Imaging (IPI), SIAM Journal on Imaging Sciences, ICLR 2025.