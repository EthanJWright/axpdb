import React, { Component } from 'react';
import './App.css';
import { render } from 'react-dom';
import 'bootstrap/dist/css/bootstrap.min.css';
import { Navbar, NavbarBrand, NavbarToggler, NavItem, Nav, NavLink, Collapse, Container } from 'reactstrap';
import Deck from './components/Deck.js'
// import axios from 'axios';


export default class PageNav extends React.Component {
    constructor(props) {
        super(props);

        this.toggle = this.toggle.bind(this);
        this.state = {
            isOpen: false
        };
    }
    toggle() {
        this.setState({
            isOpen: !this.state.isOpen
        });
    }
    render() {
        return (
            <div>
                <Navbar color="light" light expand="md">
                    <NavbarBrand href="/">AXPDB</NavbarBrand>
                    <NavbarToggler onClick={this.toggle} />
                    <Collapse isOpen={this.state.isOpen} navbar>
                        <Nav className="ml-auto" navbar>
                            <NavItem>
                                <NavLink >Free Thought</NavLink>
                            </NavItem>
                        </Nav>
                    </Collapse>
                </Navbar>
            </div>
        );
    }
}

class App extends Component {
    constructor() {
        super();
        this.onFormSubmit = this.onFormSubmit.bind(this);
        this.state = {
            Search: ""
        };
    }
    onFormSubmit() {
        // pass
    }


    render() {
        const cards = [{title: "Hey"}, {title: "There"}, {title: "Another"}];
        return (
            <div>
                <PageNav />
                <Container>
                    <Deck cards={cards}/>
                </Container>
            </div>
        );
    }
}

render(<App />, document.getElementById('root'));

