from rest_framework.serializers import (ModelSerializer, ListSerializer,
                                        IntegerField, CharField,
                                        SerializerMethodField)

from library_sample_shared.models import IndexType
from .models import LibraryPreparation


class LibraryPreparationListSerializer(ListSerializer):

    def update(self, instance, validated_data):
        # Maps for id->instance and id->data item.
        object_mapping = {obj.pk: obj for obj in instance}
        data_mapping = {item['pk']: item for item in validated_data}

        # Perform updates
        ret = []
        for obj_id, data in data_mapping.items():
            obj = object_mapping.get(obj_id, None)
            if obj is not None:
                if 'concentration_sample' in data.keys():
                    obj.sample.concentration = data['concentration_sample']
                if 'comments_facility' in data.keys():
                    obj.sample.comments_facility = data['comments_facility']
                obj.sample.save(
                    update_fields=['concentration', 'comments_facility'])

                if 'quality_check' in data.keys():
                    if data['quality_check'] == 'passed':
                        obj.sample.status = 3
                    elif data['quality_check'] == 'failed':
                        obj.sample.status = -1
                    obj.sample.save(update_fields=['status'])

                ret.append(self.child.update(obj, data))
        return ret


class LibraryPreparationSerializer(ModelSerializer):
    pk = IntegerField()
    name = SerializerMethodField()
    barcode = SerializerMethodField()
    request_name = SerializerMethodField()
    pool_name = SerializerMethodField()
    is_converted = SerializerMethodField()
    library_protocol = SerializerMethodField()
    library_protocol_name = SerializerMethodField()
    concentration_sample = SerializerMethodField()
    dilution_factor = SerializerMethodField()
    comments_facility = SerializerMethodField()
    index_i7_id = SerializerMethodField()
    index_i5_id = SerializerMethodField()
    quality_check = CharField(required=False)

    class Meta:
        model = LibraryPreparation
        list_serializer_class = LibraryPreparationListSerializer
        fields = ('pk', 'name', 'barcode', 'is_converted', 'request_name',
                  'pool_name',  'library_protocol', 'library_protocol_name',
                  'concentration_sample', 'starting_amount', 'pcr_cycles',
                  'spike_in_description', 'spike_in_volume', 'dilution_factor',
                  'comments', 'concentration_library', 'mean_fragment_size',
                  'qpcr_result', 'nM', 'comments_facility', 'index_i7_id',
                  'index_i5_id', 'quality_check',)

    def to_internal_value(self, data):
        internal_value = super().to_internal_value(data)

        concentration_sample = data.get('concentration_sample', None)
        comments_facility = data.get('comments_facility', None)

        if concentration_sample:
            try:
                internal_value.update({
                    'concentration_sample': float(concentration_sample)
                })
            except ValueError:
                pass

        if comments_facility:
            internal_value.update({
                'comments_facility': comments_facility
            })

        return internal_value

    def get_name(self, obj):
        return obj.sample.name

    def get_barcode(self, obj):
        return obj.sample.barcode

    def get_request_name(self, obj):
        return obj.sample.request.get().name

    def get_pool_name(self, obj):
        return obj.sample.pool.get().name

    def get_is_converted(self, obj):
        return obj.sample.is_converted

    def get_library_protocol(self, obj):
        return obj.sample.library_protocol.pk

    def get_library_protocol_name(self, obj):
        return obj.sample.library_protocol.name

    def get_concentration_sample(self, obj):
        return obj.sample.concentration

    def get_dilution_factor(self, obj):
        return obj.sample.dilution_factor

    def get_comments_facility(self, obj):
        return obj.sample.comments_facility

    def get_index_i7_id(self, obj):
        try:
            index_type = IndexType.objects.get(pk=obj.sample.index_type.pk)
            index_i7 = index_type.indices_i7.get(index=obj.sample.index_i7)
            return index_i7.index_id
        except Exception:
            return ''

    def get_index_i5_id(self, obj):
        try:
            index_type = IndexType.objects.get(pk=obj.sample.index_type.pk)
            index_i5 = index_type.indices_i5.get(index=obj.sample.index_i5)
            return index_i5.index_id
        except Exception:
            return ''
