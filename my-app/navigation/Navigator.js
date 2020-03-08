import { createStackNavigator } from 'react-navigation';
import Home from './HomeScreen';

const AppNavigator = createStackNavigator({
  Home: { screen: Home },
});

export default AppNavigator;