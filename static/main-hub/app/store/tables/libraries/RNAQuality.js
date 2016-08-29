Ext.define('MainHub.store.tables.libraries.RNAQuality', {
    extend: 'Ext.data.Store',
    storeId: 'rnaQualityStore',

    requires: [
        'MainHub.model.tables.libraries.LibraryField'
    ],

    model: 'MainHub.model.tables.libraries.LibraryField',

    proxy: {
        type: 'ajax',
        url: 'get_rna_qualities/',
        timeout: 1000000,
        pageParam: false,   //to remove param "page"
        startParam: false,  //to remove param "start"
        limitParam: false,  //to remove param "limit"
        noCache: false,     //to remove param "_dc",
        reader: {
            type: 'json',
            rootProperty: 'data',
            successProperty: 'success'
        }
    },

    listeners: {
        load: function(store, records, success, operation) {
            if (!success) {
                var response = operation._response,
                    obj = Ext.JSON.decode(response.responseText);
                console.log('[ERROR]: get_organisms(): ' + obj.error);
                console.log(response);
            }
        }
    }
});
