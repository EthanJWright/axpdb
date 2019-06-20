
import React from 'react';
import Video from './Video.js'
import { CardDeck } from 'reactstrap';

class Deck extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            isShow: true,
        };
    }
    render() {
        const built = [];
        
        for( var i = 0; i < this.props.cards.length; i++ ) {
            const card = this.props.cards[i];
            built.push(<Video title={card.title} />);
        }
        return (
            <CardDeck>
                {built}
            </CardDeck>
    );
    }
}

export default Deck;
