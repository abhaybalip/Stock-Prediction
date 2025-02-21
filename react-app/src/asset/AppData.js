
import Home from '../component/Home'
import Team from '../component/Team'
import Predict from '../component/Predict'

const NavList = [
    {
        name: 'Home', path: '/', component: Home
    }, {
        name: 'Team', path: '/team', component: Team
    }, {
        name: 'Predict', path: '/predict', component: Predict
    }
]

export { NavList };
