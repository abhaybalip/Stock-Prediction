import Home from '../component/Home';
import Team from '../component/Team';
import Predict from '../component/Predict';

import { FaGithub, FaLinkedin } from 'react-icons/fa6';
import { CiMail } from "react-icons/ci";

const NavList = [
    {
        name: 'Home',
        path: '/',
        component: Home
    },
    {
        name: 'Predictor',
        path: '/predict',
        component: Predict
    },
    {
        name: 'Team',
        path: '/team',
        component: Team
    },
]

const defaultLinks = [
    { name: 'email', logo: CiMail },
    { name: 'github', logo: FaGithub },
    { name: 'linkedin', logo: FaLinkedin },
]

const TeamData = [
    {
        name: 'Abhay Balip',
        links: [
            { ...defaultLinks[0], link: 'mailto:abhay.balip@gmail.com' },
            { ...defaultLinks[1], link: 'https://github.com/abhaybalip/' },
            { ...defaultLinks[2], link: 'https://linkedin.com/in/abhaybalip/' },
        ],
    },
    {
        name: 'Shyam Kamble',
        links: [
            { ...defaultLinks[0], link: 'mailto:shyam.kamble@gmail.com' },
            { ...defaultLinks[1], link: 'https://github.com/shyamkamble/' },
            { ...defaultLinks[2], link: 'https://linkedin.com/in/shyamkamble/' },
        ],
    },
    {
        name: 'Raj Malanadkar',
        links: [
            { ...defaultLinks[0], link: 'mailto:raj.malanadkar@gmail.com' },
            { ...defaultLinks[1], link: 'https://github.com/rajmalanadkar/' },
            { ...defaultLinks[2], link: 'https://linkedin.com/in/rajmalanadkar/' },
        ],
    },
    {
        name: 'Hamza Patel',
        links: [
            { ...defaultLinks[0], link: 'mailto:hamza.patel@gmail.com' },
            { ...defaultLinks[1], link: 'https://github.com/hamzapatel/' },
            { ...defaultLinks[2], link: 'https://linkedin.com/in/hamzapatel/' },
        ],
    },
]

export { NavList, TeamData }
