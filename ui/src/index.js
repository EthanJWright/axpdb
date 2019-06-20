import React, { Component } from 'react';
import './App.css';
import { render } from 'react-dom';
import 'bootstrap/dist/css/bootstrap.min.css';
import { Navbar, NavbarBrand, NavbarToggler, NavItem, Nav, NavLink, Collapse, Container } from 'reactstrap';
import Deck from './components/Deck.js'
import axios from 'axios';


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

function get_videos() {
    const options = {
        url: "http://localhost:8080/api/videos",
        headers: { "content-type": "application/json"  },
        method: "get"
    };
    return axios(options).then( (res) => {
        return res.data;
    });
}

class App extends Component {
    constructor() {
        super();
        this.onFormSubmit = this.onFormSubmit.bind(this);
        this.state = {
            cards: [{title: "Hey"}, {title: "There"}, {title: "Another"}],
            Search: ""
        };
    }
    onFormSubmit() {
        // pass
    }

    render() {
        get_videos().then( (res) => {
            this.setState({cards: res.slice(1,3)});
        });
        return (
            <div>
                <PageNav />
                <Container>
                    <Deck cards={this.state.cards}/>
                </Container>
            </div>
        );
    }
}

render(<App />, document.getElementById('root'));

