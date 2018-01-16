"""Builder for CentraXX parameters XML"""

import pyxb.utils.domutils
import xml.dom.minidom
from pyxb.namespace import XMLSchema_instance as xsi
from pyxb.namespace import XMLNamespaces as xmlns
import mtbconverter.cxxpy as cx
from . import cx_utils as cxu

class Parameters():

    def __init__(self):
        pyxb.utils.domutils.BindingDOMSupport.DeclareNamespace(cx.Namespace, 'cxx')
        self._root = cx.CentraXXDataExchange()
        self._source = 'XML-IMPORT'
        self._catalogue_data = cx.CatalogueDataType()
        self._paramsforssnv()
    
    def _paramsforssnv(self):
        """Call methods for somatic SNV parameter definition"""
        flexible_value_ci = cx.FlexibleValuesType()
        self._addchromosomes(flexible_value_ci)
        self._addeffects(flexible_value_ci)
        self._addstart(flexible_value_ci)
        self._addref(flexible_value_ci)
        self._catalogue_data.append(flexible_value_ci)
    
    def _addstart(self, flexible_value_ci):
        """Add the start position of the somatic SNV"""
        flex_type = cx.FlexibleIntegerType()
        flex_type.Code = "{}start".format(cxu.CV_PREFIX)
        flex_type.Name = "Start of SNV"
        flex_type.ShortName = "Start"
        flex_type.Description = "Start position of SNV"

        multi_entry_type_de = cx.MultilingualEntryType(Lang='de', Value='start')
        multi_entry_type_en = cx.MultilingualEntryType(Lang='en', Value='start')
        multi_entry_type_de_desc = cx.MultilingualEntryType(Lang='de', Value='start')
        multi_entry_type_en_desc = cx.MultilingualEntryType(Lang='en', Value='start')

        flex_type.NameMultilingualEntries = [multi_entry_type_de, multi_entry_type_en]
        flex_type.DescMultilingualEntries = [multi_entry_type_de_desc, multi_entry_type_en_desc]

        flexible_value_ci.append(flex_type)

    def _addref(self, flexible_value_ci):
        """Adds the reference base enumeration"""
        flex_enum_value = cx.FlexibleEnumerationType()
        flex_enum_value.Code = "{}ref".format(cxu.CV_PREFIX)
        flex_enum_value.Name = "Reference base"
        flex_enum_value.ShortName = "Reference"
        flex_enum_value.ChoiseType = "SELECTONE"
        flex_enum_value.Description = "Enumeration of different reference bases"

        multi_entry_type_de = cx.MultilingualEntryType(Lang='de', Value='ref')
        multi_entry_type_en = cx.MultilingualEntryType(Lang='en', Value='ref')
        multi_entry_type_de_desc = cx.MultilingualEntryType(Lang='de', Value='ref')
        multi_entry_type_en_desc = cx.MultilingualEntryType(Lang='en', Value='ref')

        flex_enum_value.NameMultilingualEntries = [multi_entry_type_de, multi_entry_type_en]
        flex_enum_value.DescMultilingualEntries = [multi_entry_type_de_desc, multi_entry_type_en_desc]

        flex_enum_value.UsageEntryTypeRef = ["{}{}".format(cxu.CV_PREFIX, ref) for ref in cxu.CV_BASES]
        flexible_value_ci.append(flex_enum_value)
    
    def _addalt(self, flexible_value_ci):
        pass
    
    def _addallelefreq(self, flexible_value_ci):
        pass

    def _addcoverage(self, flexible_value_ci):
        pass
    
    def _addgene(self, flexible_value_ci):
        pass
    
    def _addbasechange(self, flexible_value_ci):
        pass
    
    def _addaachange(self, flexible_value_ci):
        pass
    
    def _addtranscript(self, flexible_value_ci):
        pass
    
    def _addfunctionalclass(self, flexible_value_ci):
        pass

    def _addeffects(self, flexible_value_ci):
        """Adds the effects of the somatic SNVs"""
        flex_enum_value = cx.FlexibleEnumerationType()
        flex_enum_value.Code = "{}effect".format(cxu.CV_PREFIX)
        flex_enum_value.Name = "Effect of SNV"
        flex_enum_value.ShortName = "Effect"
        flex_enum_value.ChoiseType = "SELECTONE"
        flex_enum_value.Description = "Enumeration of different effects resulting from the variant"

        multi_entry_type_de = cx.MultilingualEntryType(Lang='de', Value='effect')
        multi_entry_type_en = cx.MultilingualEntryType(Lang='en', Value='effect')
        multi_entry_type_de_desc = cx.MultilingualEntryType(Lang='de', Value='effect')
        multi_entry_type_en_desc = cx.MultilingualEntryType(Lang='en', Value='effect')

        flex_enum_value.NameMultilingualEntries = [multi_entry_type_de, multi_entry_type_en]
        flex_enum_value.DescMultilingualEntries = [multi_entry_type_de_desc, multi_entry_type_en_desc]

        flex_enum_value.UsageEntryTypeRef = ["{}{}".format(cxu.CV_PREFIX, effect) for effect in cxu.CV_EFFECT_SSNV]
        flexible_value_ci.append(flex_enum_value)

    def _addchromosomes(self, flexible_value_ci):
        """Adds the chromosome enumerations"""
        flex_enum_value = cx.FlexibleEnumerationType()
        flex_enum_value.Code = "{}chr".format(cxu.CV_PREFIX)
        flex_enum_value.Name = "Chromosome Enumeration"
        flex_enum_value.ShortName = "chr"
        flex_enum_value.ChoiseType = "SELECTONE"
        flex_enum_value.Description = "Chromosome enumeration of the human chromosomes."
        
        multi_entry_type_de = cx.MultilingualEntryType(Lang='de', Value='Chromosome')
        multi_entry_type_en = cx.MultilingualEntryType(Lang='en', Value='Chromosome')

        multi_entry_type_de_desc = cx.MultilingualEntryType(Lang='de', Value='Chromosome')
        multi_entry_type_en_desc = cx.MultilingualEntryType(Lang='en', Value='Chromosome')

        flex_enum_value.NameMultilingualEntries = [multi_entry_type_de, multi_entry_type_en]
        flex_enum_value.DescMultilingualEntries = [multi_entry_type_de_desc, multi_entry_type_en_desc]

        flex_enum_value.UsageEntryTypeRef = ["{}{}{}".format(cxu.CV_PREFIX,'chr',index) for index in cxu.CV_CHROMOSOMES]
        flexible_value_ci.append(flex_enum_value)

    def getXML(self):
        """Write the XML object into an XML
        file"""
        self._root.Source = self._source
        self._root.CatalogueData = self._catalogue_data
        root_dom = self._root.toDOM()
        root_dom.documentElement.setAttributeNS(
            xsi.uri(), 'xsi:schemaLocation',
            'http://www.kairos-med.de ../CentraXXExchange.xsd')
        root_dom.documentElement.setAttributeNS(
            xmlns.uri(), 'xmlns:xsi', xsi.uri())
        return root_dom.toprettyxml(encoding='utf-8')