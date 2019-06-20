import React from 'react';
import { Card, CardImg, CardText, CardBody,
  CardTitle, CardSubtitle, Button } from 'reactstrap';


class Video extends React.Component {
    render() {
        //        this.texts = this.props.card.processed_description.map( (elem) => {
        //            <CardText>{elem.caller}<CardText/>
        //        });

        return (
                <Card>
                    <CardBody>
                    <CardTitle>{this.props.card.title}</CardTitle>
                    <CardSubtitle>{this.props.card.main_host}</CardSubtitle>
                    <CardText>Test</CardText>
                    <CardText>Test</CardText>
                    <CardText>Test</CardText>
                    <CardText>Test</CardText>
                    <Button>Button</Button>
                    </CardBody>
                </Card>
    );
    }
}

export default Video;
