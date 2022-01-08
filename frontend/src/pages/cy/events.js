import tippy from 'tippy.js';

export function makePopper(cy) {
    cy.ready(() => cy.elements().forEach((node) => {
        const data = node.data()
        if (!data.tip) { return }

        node.tippy = tippy(document.createElement('div'), {
        getReferenceClientRect: node.popperRef().getBoundingClientRect,
        trigger: 'manual',    
        content: () => {
          let content = document.createElement('div');
          content.classList.add("popper-div");
          content.innerHTML = `${data.tip}`;
          return content;
          }
        });    
    }));
    cy.elements().unbind('mouseover');
    cy.elements().unbind('mouseout');
    cy.elements().bind('mouseover', (event) => event.target.tippy && event.target.tippy.show());
    cy.elements().bind('mouseout', (event) => event.target.tippy && event.target.tippy.hide());
}

export function makeEvents(cy) {
    var view_utils = cy.viewUtilities({
    });
  
    makePopper(cy)

    cy.cxtmenu({
		selector: 'node',
			commands: [
				{
					content: '<span style="font-size: 2em;" class="material-icons">delete</span>',
					select: (event) => view_utils.hide(event)
				},
			],
      fillColor: 'rgba(88, 166, 255, 0.75)',
      activeFillColor: 'rgba(88, 166, 255, 1)',

	});

  cy.on('tap', function(event){
    if( event.target === cy ){
      cy.nodes().forEach(n => n.removeClass('highlight'))
      cy.edges().forEach(n => n.removeClass('highlight'))
    }
  });

  cy.on('tap', 'node', function(event){
    cy.nodes().forEach(n => n.removeClass('highlight'))
    cy.edges().forEach(n => n.removeClass('highlight'))

    event.target.incomers().forEach(e => {
      e.addClass('highlight');
        /*e.outgoers().forEach(e => e.addClass("highlight"))
        e.incomers().forEach(e => e.addClass("highlight"))*/
    })
    event.target.outgoers().forEach(e => {
      e.addClass('highlight');
        /*
        e.outgoers().forEach(e => e.addClass("highlight"))
        e.incomers().forEach(e => e.addClass("highlight"))
        */
    })

  });
}