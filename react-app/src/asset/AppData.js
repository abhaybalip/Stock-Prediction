
import Home from '../component/Home'
import Team from '../component/Team'
import Predict from '../component/Predict'

import { FaGithub, FaLinkedin } from 'react-icons/fa6';
import { CiMail } from "react-icons/ci";

const NavList = [
    {
        name: 'Home', path: '/', component: Home
    }, {
        name: 'Predictor', path: '/predict', component: Predict
    }, {
        name: 'Team', path: '/team', component: Team
    },
]

const TeamData = [

    {
        name: 'Abhay Balip',
        links: [
            { name: 'email', link: 'mailto:abhay.balip01@gmail.com', logo: CiMail },
            { name: 'github', link: 'https://github.com/abhaybalip/', logo: FaGithub },
            { name: 'linkedin', link: 'https://linkedin.com/in/abhaybalip/', logo: FaLinkedin },
        ],
    },
    {
        name: 'Hamza Patel',
        links: [
            { name: 'email', link: 'mailto:abhay.balip01@gmail.com', logo: CiMail },
            { name: 'github', link: 'https://github.com/abhaybalip/', logo: FaGithub },
            { name: 'linkedin', link: 'https://linkedin.com/in/abhaybalip/', logo: FaLinkedin },
        ],
    },
    {
        name: 'Raj Malanadkar',
        links: [
            { name: 'email', link: 'mailto:abhay.balip01@gmail.com', logo: CiMail },
            { name: 'github', link: 'https://github.com/abhaybalip/', logo: FaGithub },
            { name: 'linkedin', link: 'https://linkedin.com/in/abhaybalip/', logo: FaLinkedin },
        ],
    },
    {
        name: 'Shyam Kamble',
        links: [
            { name: 'email', link: 'mailto:abhay.balip01@gmail.com', logo: CiMail },
            { name: 'github', link: 'https://github.com/abhaybalip/', logo: FaGithub },
            { name: 'linkedin', link: 'https://linkedin.com/in/abhaybalip/', logo: FaLinkedin },
        ],
    },
]
export { NavList, TeamData };
