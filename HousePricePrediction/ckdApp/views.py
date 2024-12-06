from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect
#from .forms import *
from django.contrib import messages
from django.shortcuts import render
from django.urls import reverse_lazy
from django.urls import reverse
from django.http import HttpResponse
from django.views.generic import (View,TemplateView,
ListView,DetailView,
CreateView,DeleteView,
UpdateView)
from . import models
from .forms import *
from django.core.files.storage import FileSystemStorage
#from topicApp.Topicfun import Topic
#from ckdApp.funckd import ckd
#from sklearn.tree import export_graphviz #plot tree
#from sklearn.metrics import roc_curve, auc #for model evaluation
#from sklearn.metrics import classification_report #for model evaluation
##from sklearn.model_selection import train_test_split
#X_train, X_test, y_train, y_test = train_test_split(df2.drop('classification_yes', 1), df2['classification_yes'], test_size = .2, random_state=10)

import time
import pandas as pd
import numpy as np
#from sklearn.preprocessing import StandardScaler
#from sklearn.feature_selection import SelectKBest
#from sklearn.feature_selection import chi2
#from sklearn.model_selection import train_test_split
#from sklearn.decomposition import PCA
#from sklearn.feature_selection import RFE
#from sklearn.linear_model import LogisticRegression
import pickle
import matplotlib.pyplot as plt
#import eli5 #for purmutation importance
#from eli5.sklearn import PermutationImportance
#import shap #for SHAP values
#from pdpbox import pdp, info_plots #for partial plots
np.random.seed(123) #ensure reproduc
class dataUploadView(View):
    form_class = ckdForm
    success_url = reverse_lazy('success')
    template_name = 'create.html'
    failure_url= reverse_lazy('fail')
    filenot_url= reverse_lazy('filenot')
    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})
    def post(self, request, *args, **kwargs):
        #print('inside post')
        form = self.form_class(request.POST, request.FILES)
        #print('inside form')
        if form.is_valid():
            form.save()
            data_area= request.POST.get('area')
            data_bed=request.POST.get('bedrooms')
            data_bath=request.POST.get('bathrooms')
            data_stories=request.POST.get('stories')
            data_park=request.POST.get('parking')
            data_mainroad=request.POST.get('mainroad_yes')
            data_guestroom=request.POST.get('guestroom_yes')
            data_basement=request.POST.get('basement_yes')
            data_hotwaterheating=request.POST.get('hotwaterheating_yes')
            data_airconditioning=request.POST.get('airconditioning_yes')
            data_prefarea=request.POST.get('prefarea_yes')
            data_furnishingstatus_semi_furnished=request.POST.get('furnishingstatus_semi_furnished')
            data_furnishingstatus_unfurnished=request.POST.get('furnishingstatus_unfurnished')
            #print (data)
            #dataset1=pd.read_csv("prep.csv",index_col=None)
            #dicc={'yes':1,'no':0}
            filename = 'modelfinal.sav'
            classifier = pickle.load(open(filename, 'rb'))

            data = np.array([data_area,data_bed,data_bath,data_stories,data_park,data_mainroad,data_guestroom,data_basement,data_hotwaterheating,data_airconditioning,data_prefarea,data_furnishingstatus_semi_furnished,data_furnishingstatus_unfurnished])
            #sc = StandardScaler()
            #data = sc.fit_transform(data.reshape(-1,1))
            out=classifier.predict(data.reshape(1,-1))
# providing an index
            #ser = pd.DataFrame(data, index =['bgr','bu','sc','pcv','wbc'])

            #ss=ser.T.squeeze()
#data_for_prediction = X_test1.iloc[0,:].astype(float)

#data_for_prediction =obj.pca(np.array(data_for_prediction),y_test)
            #obj=ckd()
            ##plt.savefig("static/force_plot.png",dpi=150, bbox_inches='tight')







            return render(request, "succ_msg.html", {'data_area':data_area,'data_bed':data_bed,'data_bath':data_bath,'data_stories':data_stories,'data_park':data_park,'data_mainroad':data_mainroad,'data_guestroom':data_guestroom,'data_basement':data_basement,'data_hotwaterheating':data_hotwaterheating,'data_airconditioning':data_airconditioning,'data_prefarea':data_prefarea,
            'data_furnishingstatus_semi_furnished':data_furnishingstatus_semi_furnished,'data_furnishingstatus_unfurnished':data_furnishingstatus_unfurnished,'out':out})


        else:
            return redirect(self.failure_url)
