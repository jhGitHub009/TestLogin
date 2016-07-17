from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.contrib.auth.models import User
from django.db.models import Sum

# Create your views here.
from .models import *
from customers.models import *

def index(request):
	try:
		material_list = Material.objects.all().order_by('material_name').order_by('customer')
	except:
		raise Http404('Nothing material')
	context = {'material_list': material_list, 'customer':'Total',}
	return render(request, 'materials/index.html', context)

def index_detail(request, customer_id):
	try:
		customer = Customer.objects.get(id=customer_id)
	except:
		raise Http404('Nothing material')
	material_list = customer.material_set.all().order_by('material_name')
	context = {'material_list': material_list,'customer':customer}
	return render(request, 'materials/index.html', context)

def incoming(request):
	try:
		incoming_list = Incoming.objects.all().order_by('incoming_date')
	except:
		raise Http404('Nothing information')
	context = {'incoming_list':incoming_list}
	return render(request, 'materials/incoming.html', context)
	
def incoming_material(request, material_id):
	try:
		material = Material.objects.get(id=material_id)
	except:
		raise Http404('Nothing information')
	incoming_list = material.incoming_set.all().order_by('material')
	context = {'incoming_list':incoming_list}
	return render(request, 'materials/incoming.html', context)

def incoming_pallet(request, pallet_id):
	try:
		pallet = Pallet.objects.get(id=pallet_id)
	except:
		raise Http404('Nothing information')
	incoming_list = pallet.incoming_set.all().order_by('material')
	context = {'incoming_list':incoming_list}
	return render(request, 'materials/incoming.html', context)

def incoming_zone(request, zone_id):
	try:
		zone = Zone.objects.get(id = zone_id)
		pallets = zone.pallet_set.all()
	except:
		raise Http404('Nothing information')
	pallet_id = []
	for pallet in pallets:
		pallet_id.append(pallet.id)
	incoming_list = []
	for id in pallet_id:
		incoming = Incoming.objects.filter(pallet_id = id)
		incoming_list += incoming
	context = {'incoming_list':incoming_list}
	return render(request, 'materials/incoming.html', context)

def incoming_customer(request, customer_id):
	try:
		customer = Customer.objects.get(id=customer_id)
		materials = customer.material_set.all()
	except:
		raise Http404('Nothing information')
	material_id =[]
	for material in materials:
		material_id.append(material.id)
	incoming_list = []
	for id in material_id:
		incoming = Incoming.objects.filter(material_id=id)
		incoming_list += incoming
	context = {'incoming_list':incoming_list}
	return render(request, 'materials/incoming.html', context)

def outgoing(request):
	try:
		outgoing_list = Outgoing.objects.all().order_by('outgoing_date')
	except:
	 	raise Http404('Nothing information')
	context = {'outgoing_list':outgoing_list}
	return render(request, 'materials/outgoing.html', context)

def outgoing_material(request, material_id):
	try:
		material = Material.objects.get(id=material_id)
	except:
		raise Http404('Nothing information')
	outgoing_list = material.outgoing_set.all().order_by('material')
	context = {'outgoing_list':outgoing_list}
	return render(request, 'materials/outgoing.html', context)

def outgoing_pallet(request, pallet_id):
	try:
		pallet = Pallet.objects.get(id=pallet_id)
	except:
		raise Http404('Nothing information')
	outgoing_list = pallet.outgoing_set.all().order_by('material')
	context = {'outgoing_list':outgoing_list}
	return render(request, 'materials/outgoing.html', context)

def outgoing_zone(request, zone_id):
	try:
		zone = Zone.objects.get(id = zone_id)
		pallets = zone.pallet_set.all()
	except:
		raise Http404('Nothing information')
	pallet_id = []
	for pallet in pallets:
		pallet_id.append(pallet.id)
	outgoing_list = []
	for id in pallet_id:
		outgoing = Outgoing.objects.filter(pallet_id = id)
		outgoing_list += outgoing
	context = {'outgoing_list':outgoing_list}
	return render(request, 'materials/outgoing.html', context)

def outgoing_customer(request, customer_id):
	try:
		customer = Customer.objects.get(id=customer_id)
		materials = customer.material_set.all()
	except:
		raise Http404('Nothing information')
	material_id =[]
	for material in materials:
		material_id.append(material.id)
	outgoing_list = []
	for id in material_id:
		outgoing = Outgoing.objects.filter(material_id=id)
		outgoing_list += outgoing
	context = {'outgoing_list':outgoing_list}
	return render(request, 'materials/outgoing.html', context)

def submit(request):
	return HttpResponse("Star WooChang Material ERP")

def result(request, customer_id=''):
	if customer_id == '':
		material_list = Material.objects.all()
	else:
		try:
			customer = Customer.objects.get(id=customer_id)
			material_list = customer.material_set.all()
		except:
			raise Http404('Nothing information')
	packing_list = Packing.objects.all()
	unit_list = Unit.objects.all()
	material_result = []
	for material in material_list:
		result={}
		result['customer'] = material.customer
		result['material_id'] = material.id
		result['material_name'] = material.material_name
		result['material_code'] = material.material_code
		result['control_code'] = material.control_code
		incoming_unpack_box_counts = Incoming.objects.filter(material_id=material.id).aggregate(Sum('unpackBox_count'))
		outgoing_unpack_box_counts = Outgoing.objects.filter(material_id=material.id).aggregate(Sum('unpackBox_count'))
		if (incoming_unpack_box_counts['unpackBox_count__sum'] or outgoing_unpack_box_counts['unpackBox_count__sum']):
			if (incoming_unpack_box_counts['unpackBox_count__sum'] and outgoing_unpack_box_counts['unpackBox_count__sum']):
				result['unpacking_Box'] = incoming_unpack_box_counts['unpackBox_count__sum'] + outgoing_unpack_box_counts['unpackBox_count__sum']
			elif incoming_unpack_box_counts['unpackBox_count__sum']:
				result['unpacking_Box'] = incoming_unpack_box_counts['unpackBox_count__sum']
			else:
				result['unpacking_Box'] = outgoing_unpack_box_counts['unpackBox_count__sum']
		count_result = {}
		for unit in unit_list:
			incoming_counts = Incoming.objects.filter(material_id=material.id, incoming_unit_id=unit.id).aggregate(Sum('incoming_count'))
			outgoing_counts = Outgoing.objects.filter(material_id=material.id, outgoing_unit_id=unit.id).aggregate(Sum('outgoing_count'))
			if (incoming_counts['incoming_count__sum'] or outgoing_counts['outgoing_count__sum']):
				if ( incoming_counts['incoming_count__sum'] and outgoing_counts['outgoing_count__sum'] ):
					count_result[unit.unit_code] = incoming_counts['incoming_count__sum'] - outgoing_counts['outgoing_count__sum']
				elif incoming_counts['incoming_count__sum']:
					count_result[unit.unit_code] = incoming_counts['incoming_count__sum']
				else:
					count_result[unit.unit_code] = int('-'+str(outgoing_counts['outgoing_count__sum']))
			else :
				count_result[unit.unit_code] = 0
		result['TTL_PALLET'] = count_result['PALLET']
		result['TTL_BOX'] = (result['TTL_PALLET'] * material.Pallet_unit) + count_result['BOX']
		result['TTL_EA'] = (result['TTL_BOX'] * material.Box_unit) + count_result['EA']
		material_result.append(result)
	if customer_id == '':
		context = {'material_result':material_result, 'customer':'Total'}
	else:
		# context = {'material_result':material_result, 'customer':customer}
		context = {'material_result':material_result}
	return render(request, 'materials/result.html', context)

def result_detail(request, material_id=''):
	if material_id == '':
		material = Material.objects.all()
	else:
		try:
			material = Material.objects.get(id=material_id)
		except:
			raise Http404('Nothing information')
	packing_list = Packing.objects.all()
	unit_list = Unit.objects.all()
	pallets = Pallet.objects.all()
	pallet_list = []
	for pallet in pallets:
		if Incoming.objects.filter(material_id=material_id, pallet_id=pallet.id) or Outgoing.objects.filter(material_id=material_id, pallet_id=pallet.id):
			pallet_list.append(pallet.id)
	detail_result = []
	for pallet in pallet_list:
		result={}
		result['customer'] = material.customer
		result['material_name'] = material.material_name
		result['material_code'] = material.material_code
		result['control_code'] = material.control_code
		result['pallet'] = Pallet.objects.get(pk=pallet).pallet
		result['zone'] = Pallet.objects.get(pk=pallet).zone
		incoming_unpack_box_counts = Incoming.objects.filter(material_id=material_id, pallet_id=pallet).aggregate(Sum('unpackBox_count'))
		outgoing_unpack_box_counts = Outgoing.objects.filter(material_id=material_id, pallet_id=pallet).aggregate(Sum('unpackBox_count'))
		if (incoming_unpack_box_counts['unpackBox_count__sum'] or outgoing_unpack_box_counts['unpackBox_count__sum']):
			if (incoming_unpack_box_counts['unpackBox_count__sum'] and outgoing_unpack_box_counts['unpackBox_count__sum']):
				result['unpacking_Box'] = incoming_unpack_box_counts['unpackBox_count__sum'] + outgoing_unpack_box_counts['unpackBox_count__sum']
			elif incoming_unpack_box_counts['unpackBox_count__sum']:
				result['unpacking_Box'] = incoming_unpack_box_counts['unpackBox_count__sum']
			else:
				result['unpacking_Box'] = outgoing_unpack_box_counts['unpackBox_count__sum']
		count_result = {}
		for unit in unit_list:
			incoming_counts = Incoming.objects.filter(material_id=material_id, pallet_id=pallet, incoming_unit_id=unit.id).aggregate(Sum('incoming_count'))
			outgoing_counts = Outgoing.objects.filter(material_id=material_id, pallet_id=pallet, outgoing_unit_id=unit.id).aggregate(Sum('outgoing_count'))
			if (incoming_counts['incoming_count__sum'] or outgoing_counts['outgoing_count__sum']):
				if ( incoming_counts['incoming_count__sum'] and outgoing_counts['outgoing_count__sum'] ):
					count_result[unit.unit_code] = incoming_counts['incoming_count__sum'] - outgoing_counts['outgoing_count__sum']
				elif incoming_counts['incoming_count__sum']:
					count_result[unit.unit_code] = incoming_counts['incoming_count__sum']
				else:
					count_result[unit.unit_code] = int('-'+str(outgoing_counts['outgoing_count__sum']))
			else :
				count_result[unit.unit_code] = 0
		result['TTL_PALLET'] = count_result['PALLET']
		result['TTL_BOX'] = (result['TTL_PALLET'] * material.Pallet_unit) + count_result['BOX']
		result['TTL_EA'] = (result['TTL_BOX'] * material.Box_unit) + count_result['EA']
		detail_result.append(result)
	context = {'detail_result':detail_result, 'material':material.material_name}
	return render(request, 'materials/result_detail.html', context)