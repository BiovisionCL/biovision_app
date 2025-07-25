import 'package:flutter_test/flutter_test.dart';
import 'package:flutter/material.dart';
import 'package:biovision_app/core/widgets/primary_button.dart';

void main() {
  testWidgets('PrimaryButton displays text and reacts to tap', (WidgetTester tester) async {
    var pressed = false;

    await tester.pumpWidget(
      MaterialApp(
        home: Scaffold(
          body: PrimaryButton(
            text: 'Test Button',
            onPressed: () {
              pressed = true;
            },
          ),
        ),
      ),
    );

    expect(find.text('Test Button'), findsOneWidget);

    await tester.tap(find.byType(ElevatedButton));
    await tester.pump();

    expect(pressed, isTrue);
  });
}
