Ext.define('MainHub.view.librarypreparation.LibraryPreparation', {
    extend: 'Ext.container.Container',
    xtype: 'library-preparation',

    requires: [
        'MainHub.view.librarypreparation.LibraryPreparationController',
        'Ext.ux.FiddleCheckColumn'
    ],

    controller: 'library-preparation',

    anchor: '100% -1',
    layout: 'fit',

    items: [{
        xtype: 'grid',
        id: 'libraryPreparationTable',
        itemId: 'libraryPreparationTable',
        height: Ext.Element.getViewportHeight() - 64,
        header: {
            title: 'Library Preparation',
            items: [{
                xtype: 'textfield',
                itemId: 'searchField',
                emptyText: 'Search',
                width: 200
            }]
        },
        padding: 15,
        viewConfig: {
            // loadMask: false,
            stripeRows: false
            // markDirty: false
        },
        selModel: {
            type: 'spreadsheet',
            rowSelect: false
        },
        store: 'libraryPreparationStore',
        sortableColumns: false,
        columns: {
            defaults: {
                width: 80
            },
            items: [
                {
                    xtype: 'checkcolumn',
                    itemId: 'checkColumn',
                    dataIndex: 'selected',
                    tdCls: 'no-dirty',
                    width: 40
                },
                {
                    text: 'Request',
                    tooltip: 'Request ID',
                    dataIndex: 'requestName',
                    width: 150
                },
                {
                    text: 'Pool',
                    tooltip: 'Pool ID',
                    dataIndex: 'poolName',
                    width: 120
                },
                {
                    text: 'Sample',
                    tooltip: 'Sample Name',
                    dataIndex: 'name',
                    minWidth: 200,
                    flex: 1
                },
                {
                    text: 'Barcode',
                    dataIndex: 'barcode',
                    width: 95,
                    renderer: function(value) {
                        var record = Ext.getStore('libraryPreparationStore').findRecord('barcode', value);
                        return record ? record.getBarcode() : value;
                    }
                },
                {
                    text: 'Protocol',
                    tooltip: 'Library Protocol',
                    dataIndex: 'libraryProtocolName',
                    minWidth: 150
                },
                {
                    text: 'DF',
                    tooltip: 'Dilution Factor',
                    dataIndex: 'dilution_factor',
                    width: 60
                },
                {
                    text: 'ng/µl Sample',
                    tooltip: 'Concentration Sample (ng/µl)',
                    dataIndex: 'concentration_sample',
                    width: 100,
                    editor: {
                        xtype: 'numberfield',
                        decimalPrecision: 2,
                        minValue: 0
                    }
                },
                {
                    text: 'ng Start',
                    tooltip: 'Starting Amount (ng)',
                    dataIndex: 'starting_amount',
                    width: 100,
                    editor: {
                        xtype: 'numberfield',
                        decimalPrecision: 1,
                        minValue: 0
                    }
                },
                {
                    text: 'Spike-in',
                    tooltip: 'Spike-in Description',
                    dataIndex: 'spike_in_description',
                    width: 150,
                    editor: {
                        xtype: 'textfield'
                    }
                },
                {
                    text: 'µl Spike-in',
                    tooltip: 'Spike-in Volume (µl)',
                    dataIndex: 'spike_in_volume',
                    width: 100,
                    editor: {
                        xtype: 'numberfield',
                        decimalPrecision: 1,
                        minValue: 0
                    }
                },
                {
                    text: 'I7 ID',
                    tooltip: 'Index I7 ID',
                    dataIndex: 'indexI7Id',
                    width: 60
                },
                {
                    text: 'I5 ID',
                    tooltip: 'Index I5 ID',
                    dataIndex: 'indexI5Id',
                    width: 60
                },
                {
                    text: 'Cycles',
                    tooltip: 'PCR Cycles',
                    dataIndex: 'pcr_cycles',
                    editor: {
                        xtype: 'numberfield',
                        allowDecimals: false,
                        minValue: 0
                    }
                },
                {
                    text: 'ng/µl Library',
                    tooltip: 'Concentration Library (ng/µl)',
                    dataIndex: 'concentration_library',
                    width: 100,
                    editor: {
                        xtype: 'numberfield',
                        minValue: 0
                    }
                },
                {
                    text: 'qPCR (nM)',
                    tooltip: 'qPCR Result (nM)',
                    dataIndex: 'qpcr_result',
                    width: 100,
                    editor: {
                        xtype: 'numberfield',
                        minValue: 0
                    }
                },
                {
                    text: 'bp',
                    tooltip: 'Mean Fragment Size (bp)',
                    dataIndex: 'mean_fragment_size',
                    editor: {
                        xtype: 'numberfield',
                        allowDecimals: false,
                        minValue: 0
                    }
                },
                {
                    text: 'nM',
                    tooltip: '(Concentration Library (ng/µl) / (650 * Size (bp))) * 10^6',
                    dataIndex: 'nM',
                    editor: {
                        xtype: 'numberfield',
                        minValue: 0
                    }
                },
                {
                    text: 'QC Comments',
                    tooltip: 'Incoming Libraries/Samples QC Comments',
                    dataIndex: 'comments_facility',
                    width: 150,
                    editor: {
                        xtype: 'textfield'
                    }
                },
                {
                    text: 'Comments',
                    dataIndex: 'comments',
                    width: 150,
                    editor: {
                        xtype: 'textfield'
                    }
                },
                {
                    text: 'QC Result',
                    dataIndex: 'qc_result',
                    width: 90,
                    editor: {
                        xtype: 'combobox',
                        queryMode: 'local',
                        displayField: 'name',
                        valueField: 'id',
                        store: Ext.create('Ext.data.Store', {
                            fields: [
                                {
                                    name: 'id',
                                    type: 'int'
                                },
                                {
                                    name: 'name',
                                    type: 'string'
                                }
                            ],
                            data: [
                                {
                                    id: 1,
                                    name: 'passed'
                                },
                                {
                                    id: 2,
                                    name: 'failed'
                                }
                            ]
                        }),
                        forceSelection: true
                    }
                }
            ]
        },
        plugins: [
            {
                ptype: 'rowediting',
                clicksToEdit: 1
            },
            {
                ptype: 'bufferedrenderer',
                trailingBufferZone: 100,
                leadingBufferZone: 100
            },
            {
                ptype: 'clipboard'
            }
        ],
        features: [{
            ftype: 'grouping',
            startCollapsed: true,
            groupHeaderTpl: [
                '<strong>Protocol: {children:this.getName}</strong>',
                {
                    getName: function(children) {
                        return children[0].get('libraryProtocolName');
                    }
                }
            ]
        }],
        dockedItems: [{
            xtype: 'toolbar',
            dock: 'bottom',
            items: [
                {
                    xtype: 'button',
                    id: 'downloadBenchtopProtocolLPBtn',
                    itemId: 'downloadBenchtopProtocolLPBtn',
                    text: 'Download Benchtop Protocol',
                    iconCls: 'fa fa-file-excel-o fa-lg'
                    // disabled: true
                },
                '->',
                {
                    xtype: 'button',
                    itemId: 'cancelBtn',
                    iconCls: 'fa fa-ban fa-lg',
                    text: 'Cancel'
                },
                {
                    xtype: 'button',
                    itemId: 'saveBtn',
                    iconCls: 'fa fa-floppy-o fa-lg',
                    text: 'Save'
                }
            ]
        }]
    }]
});
