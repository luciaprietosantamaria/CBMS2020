#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 11:38:12 2020

@author: Lucía Prieto
"""

# Obtaining features arrays (rows:diseases, columns: vectors of boolean values
# representing whether a gene, protein, etc., is associated to a disease)

import pandas as pd

# CSV contains relationship disease - feature 
disease_gene = pd.read_csv('all_diseaseCUI_prot.csv')
disease_gene_array = disease_gene.to_numpy()

# Obtaining a numpy list of the different diseases
diseases = disease_gene['disease_id']
diseases = diseases.sort_values(ascending = True).drop_duplicates().to_numpy()

# Obtaining a numpy list of the different features (genes, proteins...)
genes = disease_gene['gene_id']
genes = genes.sort_values(ascending = True).drop_duplicates().to_numpy()

# Creating a dictionary, where the keys are the diseases 
# (values will be the features related to the disease)
dis_gen_dict = { i : list() for i in diseases}


# Completing the features of a disease in the dictionary
for [disease, gene] in disease_gene_array:
    
    if not gene in dis_gen_dict[disease]:
        dis_gen_dict[disease].append(gene)
        


# Generating the features array with zeros
bool_matr = [[0 for x in range(len(genes))] for y in range(len(diseases))] 

count_dis = 0


for dis in diseases:
    
    count_gen = 0
    
    for gen in genes:
        
        if gen in dis_gen_dict[dis]:
            
            bool_matr[count_dis][count_gen] = 1
            
        count_gen += 1
        
    count_dis += 1
    

feat_matr = pd.DataFrame(bool_matr)

feat_matr.to_csv('all_feature_matrix_prots_CUI.csv', index=False)  