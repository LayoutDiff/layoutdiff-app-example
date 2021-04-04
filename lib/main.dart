import 'package:flutter/material.dart';
import "dart:math";

void main() => runApp(LayoutDiffExample());

class _BoxDecorationState extends State<LayoutDiffBoxDecoration> {
  final List<MaterialColor> _bgColors = [Colors.blue, Colors.green, Colors.yellow, Colors.red, Colors.brown];
  MaterialColor _bgColor = Colors.blue;

  MaterialColor getRandomColor<T>() {
    
    final random = new Random();
    var i = random.nextInt(_bgColors.length);
    var color = _bgColors[i];

    if(color == _bgColor) {
      return getRandomColor();
    }

    return color;
  }
  
  @override
  Widget build(BuildContext context) {
    return Container(
      decoration: BoxDecoration(
        gradient: LinearGradient(
          begin: Alignment.topLeft,
          end: Alignment.bottomRight,
          colors: [_bgColor[100], _bgColor[500]]
        )
      ),
      child: ListView(
          padding: const EdgeInsets.all(20),
          children: <Widget>[
            Center(
              child: Text('LayoutDiff is cool!',
                style: TextStyle(
                  fontSize: 35,
                  color: Colors.white,
                ),
              ),
            ),
            ElevatedButton(            
              child: Text('Press'),
              onPressed: () {  
                setState(() {
                  _bgColor = getRandomColor();
                });
              },
            )
          ]
      )
    );
  }

}

class LayoutDiffBoxDecoration extends StatefulWidget {
  @override
  State<StatefulWidget> createState() {
    return _BoxDecorationState();
  }

}

class LayoutDiffExample extends StatelessWidget {

   @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'LayoutDiff Example',
      home: Scaffold(
        appBar: AppBar(
          title: Text('LayoutDiff Example.'),
        ),
        body: LayoutDiffBoxDecoration()
      ),
    );
  }

}
