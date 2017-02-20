from django.test import TestCase

from .models import (Organism, ConcentrationMethod, ReadLength, IndexType,
                     IndexI7, GenericIndex, BarcodeCounter,
                     GenericLibrarySample)


# Models

class OrganismTest(TestCase):
    def setUp(self):
        self.organism = Organism(name='mouse')

    def test_organism_name(self):
        self.assertTrue(isinstance(self.organism, Organism))
        self.assertEqual(self.organism.__str__(), self.organism.name)


class ConcentrationMethodTest(TestCase):
    def setUp(self):
        self.method = ConcentrationMethod(name='fluorography')

    def test_concentration_method_name(self):
        self.assertTrue(isinstance(self.method, ConcentrationMethod))
        self.assertEqual(self.method.__str__(), self.method.name)


class ReadLengthTest(TestCase):
    def setUp(self):
        self.read_length = ReadLength(name='1x50')

    def test_read_length_name(self):
        self.assertTrue(isinstance(self.read_length, ReadLength))
        self.assertEqual(self.read_length.__str__(), self.read_length.name)


class IndexTypeTest(TestCase):
    def setUp(self):
        self.index_type = IndexType(name='Nextera')

    def test_index_type_name(self):
        self.assertTrue(isinstance(self.index_type, IndexType))
        self.assertEqual(self.index_type.__str__(), self.index_type.name)


class GenericIndexTest(TestCase):
    def setUp(self):
        self.index1 = IndexI7(index_id='I001', index='ATCACG')
        self.index2 = GenericIndex(index_id='I002', index='ATCACG')
        self.index1.save()

        self.index_type = IndexType(name='Index Type', is_index_i7=True)
        self.index_type.save()
        self.index_type.indices_i7.add(self.index1)

    def test_generic_index_id(self):
        self.assertTrue(isinstance(self.index1, GenericIndex))
        self.assertEqual(self.index1.__str__(), self.index1.index_id)
        self.assertEqual(self.index1.type(), self.index_type.name)

    def test_no_index_type(self):
        self.assertEqual(self.index2.type(), '')


class BarcodeCounterTest(TestCase):
    def setUp(self):
        counter = BarcodeCounter.load()
        counter.increment()
        counter.save()

    def test_barcode_counter_name(self):
        counter = BarcodeCounter.load()
        self.assertEqual(counter.__str__(), str(counter.counter))


class GenericLibrarySampleTest(TestCase):
    def setUp(self):
        organism = Organism(name='mouse')
        concentration_method = ConcentrationMethod(name='fluorography')
        read_length = ReadLength(name='1x50')

        self.library = GenericLibrarySample(
            name='Library1',
            organism=organism,
            concentration=1.0,
            concentration_method=concentration_method,
            dna_dissolved_in='dna',
            sample_volume=1,
            read_length=read_length,
            sequencing_depth=1
        )

    def test_generic_library_sample_name(self):
        self.assertTrue(isinstance(self.library, GenericLibrarySample))
        self.assertEqual(self.library.__str__(), self.library.name)


# Fixtures

# class FixturesTestcase(TestCase):
#     fixtures = [
#         'organisms.json',
#         'concentration_methods.json',
#         'read_lengths.json',
#         'indices.json',
#     ]
#
#     def setUp(self):
#         pass
#
#     def test_loaded_fixtures(self):
#         human = Organism.objects.get(pk=1)
#         self.assertEqual(human.name, 'human')
