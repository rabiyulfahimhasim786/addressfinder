from django.shortcuts import render
from django.shortcuts import get_object_or_404
import re

# import module
from geopy.geocoders import Nominatim
# Create your views here.
from django.http import HttpResponse
import googlemaps
gmaps = googlemaps.Client(key='Your_api_key')
geolocator = Nominatim(user_agent="Your_api_key")
def index(request):
    return HttpResponse("Hello, world !")


from django.shortcuts import render,redirect
from .models import Mappin, Mapsdata, Locationadress, Locationdata
from .forms import Mappinform, Mapsdataform, Locationadressform, Locationdataform
# Create your views here.

def mapscity(request):
    #add Your_api_key in this below mapscity html
    return render(request, 'mapscity.html')

def mappin_form(request):
    if request.method == 'POST':
        form = Mappinform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            #documents = Mappin.objects.all()
            # return render(request, 'keywordform.html', {'form': form, })
            # documents = Mappin.objects.all()
            # for obj in documents:
            #     n = obj.mapurl
            # print(n)
            print('start')
            try:
                documents = Mappin.objects.all()
                for obj in documents:
                    mapurldata = obj.mapurl
                print(mapurldata)
                location = gmaps.geocode(mapurldata)
                lat = location[0]['geometry']['location']['lat']
                lng = location[0]['geometry']['location']['lng']
                address = gmaps.reverse_geocode((lat, lng))[0]['formatted_address']
                #print(address)
                adress_no = gmaps.reverse_geocode((lat, lng))[0]['address_components'][0]['long_name']
                adress_street = gmaps.reverse_geocode((lat, lng))[0]['address_components'][1]['long_name']
                adress_city = gmaps.reverse_geocode((lat, lng))[0]['address_components'][2]['long_name']
                adress_subcity = gmaps.reverse_geocode((lat, lng))[0]['address_components'][3]['long_name']
                adress_state = gmaps.reverse_geocode((lat, lng))[0]['address_components'][4]['long_name']
                adress_country = gmaps.reverse_geocode((lat, lng))[0]['address_components'][5]['long_name']
                adress_zip = gmaps.reverse_geocode((lat, lng))[0]['address_components'][6]['long_name']
                adress_zipcode = gmaps.reverse_geocode((lat, lng))[0]['address_components'][7]['long_name']
                print(len(adress_zipcode))
                searchingaddress = adress_no+', '+adress_street
                # if int(len(adress_zipcode)) > 0:
                #     addressdatasets = {'form': form,  'links':mapurldata,'searchingaddress':searchingaddress, 'adresscity':adress_state, 'adressstate':adress_country, 'addresscountry':adress_zip, 'adresszip':adress_zipcode,}
                #     print(addressdatasets)
                #     print('not none')
                #     return render(request, 'keywordform.html', addressdatasets)
                # else:
                print(adress_no)
                # print(adress_street)
                # print(adress_city)
                # print(adress_subcity)
                # print(adress_city)
                # print(adress_state)
                # print(adress_country)
                # print(adress_zip)
                # print(adress_zipcode)
                # searchingaddress = adress_no+', '+adress_street+', '+adress_streetname+', '+adress_subcity
                    #searchingaddress = adress_no+', '+adress_street
                print('ok')
                mapdata = Mapsdata.objects.create(
                        maplink=mapurldata,
                        mapaddress=searchingaddress,
                        mapcity=adress_city,
                        mapstate=adress_state,
                        mapcountry = adress_country,
                        mapzip=adress_zip,)
                mapdata.save()
                addressdatasets = {'form': form,  'links':mapurldata,'searchingaddress':searchingaddress, 'adresscity':adress_city, 'adressstate':adress_state, 'addresscountry':adress_country, 'adresszip':adress_zip, 'adress_zipcode':adress_zipcode}
                return render(request, 'keywordform.html', addressdatasets)
            except:
                #print("An exception occurred")
                # errortext = 'Plesae provide a valid URL'
                # longurl = ''
                # initialize Nominatim API
                try:
                    print('exceptif')
                    temp = re.search('@([0-9]?[0-9]\.[0-9]*),([0-9]?[0-9]\.[0-9]*)', mapurldata, re.DOTALL)
                    latitude  = temp.groups()[0]
                    longitude = temp.groups()[1]
                    geolocator = Nominatim(user_agent="Your_api_key")
                    location = geolocator.reverse(latitude+","+longitude)
                    address = location.raw['address']
                    # traverse the data
                    #Suburb = address.get('suburb', '')
                    city = address.get('city', '')
                    state = address.get('state', '')
                    country = address.get('country', '')
                    code = address.get('country_code')
                    zipcode = address.get('postcode')
                    # print('Suburb : ', suburb)
                    print('City : ', city)
                    print('State : ', state)
                    print('Country : ', country)
                    print('Zip Code : ', zipcode)
                    return render(request, 'keywordform.html', {'form': form,  'adresscity':city, 'adressstate':state, 'addresscountry':country, 'adresszip':zipcode})
                    #return render(request, 'keywordform.html', {'form': form, })
                except:
                   print('exceptelse')
                   errortext = 'Plesae provide a valid URL'
                   return render(request, 'keywordform.html', {'form': form,  'errortext':errortext,})
            
    else:
        form = Mappinform()
    return render(request, 'keywordform.html', {'form': form, })

def retrieve(request):
    details=Mapsdata.objects.all().order_by('-id')
    return render(request,'retrieve.html',{'details':details})

def edit(request,id):
    object=Mapsdata.objects.get(id=id)
    return render(request,'edit.html',{'object':object})

def update(request,id):
    object=Mapsdata.objects.get(id=id)
    form=Mapsdataform(request.POST,instance=object)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            # object=Film.objects.all()
            return redirect('retrieve')
    return redirect('retrieve')

# def delete(request,id):
#     Film.objects.filter(id=id).delete()
#     return redirect('retrieve')



def delete(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}



def location_form(request):
    if request.method == 'POST':
        form = Locationadressform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print('start')
            try:
                documents = Locationadress.objects.all()
                for obj in documents:
                    mapurldatas = obj.locationdata
                print(mapurldatas)
                location = gmaps.geocode(mapurldatas)
                lat = location[0]['geometry']['location']['lat']
                lng = location[0]['geometry']['location']['lng']
                address = gmaps.reverse_geocode((lat, lng))[0]['formatted_address']
                print(address)
                # adress_no = gmaps.reverse_geocode((lat, lng))[0]['address_components'][0]['long_name']
                # adress_street = gmaps.reverse_geocode((lat, lng))[0]['address_components'][1]['long_name']
                # adress_city = gmaps.reverse_geocode((lat, lng))[0]['address_components'][2]['long_name']
                # adress_subcity = gmaps.reverse_geocode((lat, lng))[0]['address_components'][3]['long_name']
                # adress_state = gmaps.reverse_geocode((lat, lng))[0]['address_components'][4]['long_name']
                # adress_country = gmaps.reverse_geocode((lat, lng))[0]['address_components'][5]['long_name']
                # adress_zip = gmaps.reverse_geocode((lat, lng))[0]['address_components'][6]['long_name']
                # adress_zipcode = gmaps.reverse_geocode((lat, lng))[0]['address_components'][7]['long_name']
                # addressoveralldata = adress_no+', '+adress_street+', '+adress_city+', '+adress_state+', '+adress_country+', '+adress_zip+', '+adress_zipcode
                # print(addressoveralldata)
                print('ok')
                mapdatasets = Locationdata.objects.create(
                    locationlink=mapurldatas,
                    addressdata=address,)
                mapdatasets.save()
                
                # addressdatasets = {'form': form,  'links':mapurldatas, 'address':addressoveralldata}
                return render(request, 'map.html', {'form': form,  'links':mapurldatas, 'address':address})
            except:
                #print("An exception occurred")
                # errortext = 'Plesae provide a valid URL'
                # longurl = ''
                # initialize Nominatim API
                try:
                    print('exceptif')
                    temp = re.search('@([0-9]?[0-9]\.[0-9]*),([0-9]?[0-9]\.[0-9]*)', mapurldatas, re.DOTALL)
                    latitude  = temp.groups()[0]
                    longitude = temp.groups()[1]
                    # geolocator = Nominatim(user_agent="api_key")
                    location = geolocator.reverse(latitude+","+longitude)
                    address = location.raw['address']
                    print(address)

                    # # traverse the data
                    # #Suburb = address.get('suburb', '')
                    city = address.get('city', '')
                    state = address.get('state', '')
                    country = address.get('country', '')
                    code = address.get('country_code')
                    zipcode = address.get('postcode')
                    addressdataaddon = city+', '+state+', '+country+', '+zipcode
                    # print('Suburb : ', suburb)
                    # print('City : ', city)
                    # print('State : ', state)
                    # print('Country : ', country)
                    # print('Zip Code : ', zipcode)
                    return render(request, 'map.html', {'form': form, 'address': addressdataaddon})
                    #return render(request, 'keywordform.html', {'form': form, })
                except:
                    print('exceptelse')
                    errortext = 'Plesae provide a valid URL'
                    return render(request, 'map.html', {'form': form,  'errortext':errortext,})
            
    else:
        form = Locationadressform()
    return render(request, 'map.html', {'form': form, })

def retrievedata(request):
    details=Locationdata.objects.all().order_by('-id')
    return render(request,'retrievedata.html',{'details':details})

def editdata(request,id):
    object=Locationdata.objects.get(id=id)
    return render(request,'editdata.html',{'object':object})

def updatedata(request,id):
    object=Locationdata.objects.get(id=id)
    form=Locationdataform(request.POST,instance=object)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            # object=Film.objects.all()
            return redirect('retrievedata')
    return redirect('retrievedata')

# def delete(request,id):
#     Film.objects.filter(id=id).delete()
#     return redirect('retrieve')



def deletedata(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # fetch the object related to passed id
    obj = get_object_or_404(Locationdata, id = id)
 
 
    if request.method =="POST":
        # delete object
        obj.delete()
        # after deleting redirect to
        # home page
        # return HttpResponseRedirect("/")
        return redirect('retrievedata')
 
    return render(request, "delete.html", context)