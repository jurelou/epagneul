import cytoscape from 'cytoscape';

import cxtmenu from 'cytoscape-cxtmenu';
import popper from 'cytoscape-popper';
import klay from 'cytoscape-klay';
import coseBilkent from 'cytoscape-cose-bilkent';
import fcose from 'cytoscape-fcose';
import layoutUtilities from 'cytoscape-layout-utilities';
import viewUtilities  from 'cytoscape-view-utilities';


import { style } from './style';
import { makeEvents } from './events';

cytoscape.use( cxtmenu );
cytoscape.use( layoutUtilities );
cytoscape.use( viewUtilities );

cytoscape.use( popper );
cytoscape.use( klay );
cytoscape.use( coseBilkent );
cytoscape.use( fcose );


export function makeCytoscape(elements) {
    return cytoscape({
        container: document.getElementById('cy'),
        boxSelectionEnabled: false,
        elements: elements,
        ready: function() {
          let layoutUtilities = this.layoutUtilities({
            desiredAspectRatio: 2,
            fullness: 50,
            componentSpacing: 100
          });
          makeEvents(this)
        },
        layout: {
          name: 'fcose',
          animationEasing: 'ease-in-sine',
          animate: false,      
          fit: true,
          tile: true,
          idealEdgeLength: 80,
          packComponents: false,
          nodeRepulsion: 17000
        },
        style: style,
      })
}