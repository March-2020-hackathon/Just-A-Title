import React from 'react';
import { Camera } from 'expo-camera';
import { View, Text } from 'react-native';
import * as Permissions from 'expo-permissions';
import ImgToBase64 from 'react-native-image-base64';

import Modal from "react-native-modal";



import styles from './styles';
import Toolbar from './Toolbar';
import Gallery from './Gallery';
// import Buffer from './buffer';
import Jimp from 'jimp';

export default class CameraPage extends React.Component {
    camera = null;

    state = {
        isVisible: false,
        pref: ['Vegan'],
        dataSource: null,
        captures: [],
        capture: null,
        capturing: null,
        hasCameraPermission: null,
        cameraType: Camera.Constants.Type.back,
        flashMode: Camera.Constants.FlashMode.off,
    };

    setFlashMode = (flashMode) => this.setState({ flashMode });
    setCameraType = (cameraType) => this.setState({ cameraType });
    handleCaptureIn = () => this.setState({ capturing: true });

    handleCaptureOut = () => {
        if (this.state.capturing)
            this.camera.stopRecording();
    };

    handleShortCapture = async () => {
        const photoData = await this.camera.takePictureAsync();
        this.setState({ capturing: false, captures: [photoData, ...this.state.captures] })
        // this.navigateToImgSelection(this.state.captures)
        this.uploadFile();
        this.state.isVisible = true;
        setTimeout(() => {this.state.isVisible = false;}, 3000)
        
        
    };
        

    handleLongCapture = async () => {
        const videoData = await this.camera.recordAsync();
        this.setState({ capturing: false, captures: [videoData, ...this.state.captures] });
    };

    async componentDidMount() {
        const camera = await Permissions.askAsync(Permissions.CAMERA);
        const audio = await Permissions.askAsync(Permissions.AUDIO_RECORDING);
        const hasCameraPermission = (camera.status === 'granted' && audio.status === 'granted');

        this.setState({ hasCameraPermission });
    };

    

    navigateToImgSelection(captures) {
        
        const { navigation } = this.props
        navigation.navigate('LinksScreen', {
            captures
        });
    }

    uploadFile() {
        
        Jimp.read(this.state.captures[0].uri)
            .then(image => {
                
                this.state.capture = image.bitmap.data.toString('base64')
                // console.log(this.state.capture)
                this._fetch(this.state.capture);
            })
            .catch(err => {
                console.log(err)
            })


    };

    _fetch(data){
        //'http://34.68.156.199/'
        // console.log(data)
        fetch('http://34.68.156.199/', {
            method: 'POST',
            headers: {
                Accept: 'application/json',
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                captures: data,
                pref: this.state.pref
            })
        })
        .catch(error => { 
            console.log('There has been a problem with your fetch operation: ' + error);
            // ADD THIS THROW error
            throw error;
        })
        
        
    };

    

    render() {
        const { hasCameraPermission, flashMode, cameraType, capturing, captures } = this.state;

        if (hasCameraPermission === null) {
            return <View />;
        } else if (hasCameraPermission === false) {
            return <Text>Access to camera has been denied.</Text>;
        }



        return (
            <React.Fragment>
                <View>
                    <Camera
                        type={cameraType}
                        flashMode={flashMode}
                        style={styles.preview}
                        ref={camera => this.camera = camera}
                    />

                    <Modal isVisible={this.state.isVisible}>
                      <View style={{ flex: 1, marginTop:70, textAlign: 'center', backgroundColor: 'white' }}>
                        <Text>Eat</Text>
                      </View>
                    </Modal>

                </View>

                {captures.length > 0 && <Gallery captures={captures}/>}

                <Toolbar 
                    capturing={capturing}
                    flashMode={flashMode}
                    cameraType={cameraType}
                    setFlashMode={this.setFlashMode}
                    setCameraType={this.setCameraType}
                    onCaptureIn={this.handleCaptureIn}
                    onCaptureOut={this.handleCaptureOut}
                    onLongCapture={this.handleLongCapture}
                    onShortCapture={this.handleShortCapture}
                />
            </React.Fragment>
        );
    };
};