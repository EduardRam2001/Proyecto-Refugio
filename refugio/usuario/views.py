
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import CreateView, UpdateView,ListView
from django.urls import reverse_lazy
from usuario.utils import render_to_pdf
from usuario.forms import RegistroForm, UserPerfil,PasswordEdit, AxesCaptchaForm
from django.contrib.auth.views import PasswordChangeView
from axes.utils import reset_request

#import cv2
#import os
#import imutils
#import numpy as np

	
class ListadeUsuario(ListView):
	model = User
	template_name = 'usuario/Usuariolista.html'
	context_object_name = 'usuarios'

class ListadeUsuarioPDF(ListView):
	
    def get(self, request, *args, **kwargs):
        usuarios = User.objects.all()
        data = {
            'usuarios': usuarios
        }
        pdf = render_to_pdf('usuario/Usuariolistapdf.html',data)
        return HttpResponse(pdf, content_type='application/pdf')

class RegistroUsuario( CreateView):
	model = User
	template_name = "usuario/usuarioRegistro.html"
	form_class = RegistroForm
	success_url = reverse_lazy('login')

class UsuarioPerfil(ListView):
	model = User
	template_name = "usuario/usuarioPerfil.html"
	form_class = RegistroForm


class UsuarioEditPerfil(UpdateView):
	model = User
	form_class = UserPerfil
	template_name = "usuario/usuarioActualizar.html"
	success_url = reverse_lazy('usuario_perfil')

	
class UsuarioEditContraseña(PasswordChangeView):
	form_class = PasswordEdit
	template_name = "usuario/usuarioActualizarContraseña.html"
	success_url = reverse_lazy('usuario_perfil')	



def locked_out(request):
    if request.POST:
        form = AxesCaptchaForm(request.POST)
        if form.is_valid():
            reset_request(request)
            return HttpResponseRedirect(reverse_lazy('login'))
    else:
        form = AxesCaptchaForm()

    return render(request, 'base/bloqueo.html', {'form': form})

"""
def RegistroCaras(request):
    
    nombre = User.objects.all().last()
    contexto = {'user': nombre}
    print("ultimo usuario::  ",nombre)
    
    personName =  str(nombre)
    
    dataPath = 'static/imgperfil/Data'#Cambia a la ruta donde hayas almacenado Data
    personPath = dataPath + '/' + personName
    if not os.path.exists(personPath):
        print('Carpeta creada: ',personPath)
        os.makedirs(personPath)
    cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
    
    faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
    count = 0

    while True:
        ret, frame = cap.read()
        if ret == False: break
        frame =  imutils.resize(frame, width=640)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        auxFrame = frame.copy()
    
        faces = faceClassif.detectMultiScale(gray,1.3,5)
    
        for (x,y,w,h) in faces:
            cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
            rostro = auxFrame[y:y+h,x:x+w]
            rostro = cv2.resize(rostro,(150,150),interpolation=cv2.INTER_CUBIC)
            cv2.imwrite(personPath + '/rostro_{}.jpg'.format(count),rostro)
            count = count + 1
        cv2.imshow('frame',frame)
    
        k =  cv2.waitKey(1)
        if k == 27 or count >= 100:
            break
    cap.release()
    cv2.destroyAllWindows()

    peopleList = os.listdir(dataPath)
    print('Lista de personas: ', peopleList)
    labels = []
    facesData = []
    label = 0
    for nameDir in peopleList:
        personPath = dataPath + '/' + nameDir
        print('Leyendo las imágenes')
        for fileName in os.listdir(personPath):
            #print('Rostros: ', nameDir + '/' + fileName)
            labels.append(label)
            facesData.append(cv2.imread(personPath+'/'+fileName,0))
            image = cv2.imread(personPath+'/'+fileName,0)
        label = label + 1


    face_recognizer = cv2.face.EigenFaceRecognizer_create()
    print("Entrenando...")
    face_recognizer.train(facesData, np.array(labels))

    face_recognizer.write('modeloEigenFace.xml')
    print("Modelo almacenado...")
    return render(request, 'usuario/caras.html',contexto)


def ValidarCara(request):
    
    dataPath = 'static/imgperfil/Data'#Cambia a la ruta donde hayas almacenado Data
    imagePaths = os.listdir(dataPath)
    print('imagePaths =', imagePaths)

    face_recognizer = cv2.face.EigenFaceRecognizer_create()

    face_recognizer.read('modeloEigenFace.xml')

    
    nombreVentana = "camara"
    cv2.namedWindow(nombreVentana)
    cap = cv2.VideoCapture(0)



    faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
    while True:
        ret,frame = cap.read()
        if ret == False: 
            break
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        auxFrame = gray.copy()
        faces = faceClassif.detectMultiScale(gray,1.3,5)
        for (x,y,w,h) in faces:
            rostro = auxFrame[y:y+h,x:x+w]
            rostro = cv2.resize(rostro,(150,150),interpolation= cv2.INTER_CUBIC)
            result = face_recognizer.predict(rostro)
            cv2.putText(frame,'{}'.format(result),(x,y-5),1,1.3,(255,255,0),1,cv2.LINE_AA)
        
        # EigenFaces
            if result[1] < 4600:
                cv2.putText(frame,'{}'.format(imagePaths[result[0]]),(x,y-25),2,1.1,(0,255,0),1,cv2.LINE_AA)
                cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
                print (imagePaths[result[0]])
                nombre = str(imagePaths[result[0]])
                contexto = {'user': nombre}
                print("rostro detectado exitoso")
                return render(request, 'usuario/rostro_validado.html',contexto)
            else:
                cv2.putText(frame,'Desconocido',(x,y-20),2,0.8,(0,0,255),1,cv2.LINE_AA)
                cv2.rectangle(frame, (x,y),(x+w,y+h),(0,0,255),2)
                nombre = "Desconocido"
                contexto = {'user': nombre}
                return render(request, 'usuario/rostro_invalido.html',contexto) 
        cv2.imshow(nombreVentana,frame)
        k = cv2.waitKey(1)
        if k == 27 or not cv2.getWindowProperty(nombreVentana, cv2.WND_PROP_VISIBLE):
            break

    cap.release()

    cv2.destroyAllWindows(nombreVentana)
"""
